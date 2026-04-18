#!/usr/bin/env python3
"""Fold tasks.jsonl event log into tasks.json current-state view.

Usage: python3 derive.py [--dry-run]

Event types:
  task.created   {id, ts, title, project, tier, deadline_jst?, estimated_min?, tags?, start_hour?}
  task.updated   {id, ts, ...fields}
  task.completed {id, ts, shipped?}
  task.blocked   {id, ts, blocked_on}
  task.parked    {id, ts}
  task.unparked  {id, ts}
  task.started   {id, ts}
  calendar.synced {id, ts, calendar_event_id, etag}
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

STATE_DIR = Path(__file__).parent
JSONL = STATE_DIR / "tasks.jsonl"
JSON_OUT = STATE_DIR / "tasks.json"
JS_OUT = STATE_DIR / "tasks.js"

JST = timezone(timedelta(hours=9))


def load_events():
    if not JSONL.exists():
        return []
    events = []
    with open(JSONL) as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"WARN: tasks.jsonl line {i} invalid JSON: {e}", file=sys.stderr)
    return events


def fold(events):
    tasks = {}
    for ev in events:
        ev_type = ev.get("event")
        tid = ev.get("id")
        ts = ev.get("ts")
        if not ev_type or not tid:
            continue
        if ev_type == "task.created":
            tasks[tid] = {
                "id": tid,
                "title": ev.get("title", ""),
                "project": ev.get("project", ""),
                "tier": ev.get("tier", "T2"),
                "deadline_jst": ev.get("deadline_jst"),
                "estimated_min": ev.get("estimated_min"),
                "tags": ev.get("tags", []),
                "start_hour": ev.get("start_hour"),
                "status": "active",
                "blocked_on": None,
                "calendar_event_id": None,
                "calendar_etag": None,
                "created_at": ts,
                "last_touched": ts,
                "started_at": None,
                "completed_at": None,
                "shipped": None,
            }
        elif ev_type == "task.updated":
            if tid in tasks:
                for k, v in ev.items():
                    if k in ("event", "id", "ts"):
                        continue
                    tasks[tid][k] = v
                tasks[tid]["last_touched"] = ts
        elif ev_type == "task.completed":
            if tid in tasks:
                tasks[tid]["status"] = "completed"
                tasks[tid]["completed_at"] = ts
                tasks[tid]["shipped"] = ev.get("shipped")
                tasks[tid]["last_touched"] = ts
        elif ev_type == "task.blocked":
            if tid in tasks:
                tasks[tid]["status"] = "blocked"
                tasks[tid]["blocked_on"] = ev.get("blocked_on")
                tasks[tid]["last_touched"] = ts
        elif ev_type == "task.parked":
            if tid in tasks:
                tasks[tid]["status"] = "parked"
                tasks[tid]["last_touched"] = ts
        elif ev_type == "task.unparked":
            if tid in tasks:
                tasks[tid]["status"] = "active"
                tasks[tid]["last_touched"] = ts
        elif ev_type == "task.started":
            if tid in tasks:
                tasks[tid]["started_at"] = ts
                tasks[tid]["last_touched"] = ts
        elif ev_type == "calendar.synced":
            if tid in tasks:
                tasks[tid]["calendar_event_id"] = ev.get("calendar_event_id")
                tasks[tid]["calendar_etag"] = ev.get("etag")
    return tasks


def bucket(tasks):
    today_jst = datetime.now(JST).strftime("%Y-%m-%d")
    now_jst = datetime.now(JST)
    buckets = {
        "today": [],
        "deadlines_72h": [],
        "blocked": [],
        "parked": [],
        "shipped_today": [],
        "shipped_week": [],
        "stale": [],
        "backlog": [],
    }
    for t in tasks.values():
        deadline = t.get("deadline_jst")
        status = t["status"]
        if status == "completed":
            completed_at = t.get("completed_at")
            if completed_at and completed_at.startswith(today_jst):
                buckets["shipped_today"].append(t)
            if completed_at:
                try:
                    dt = datetime.fromisoformat(completed_at.replace("Z", "+00:00"))
                    if (now_jst - dt.astimezone(JST)).days <= 7:
                        buckets["shipped_week"].append(t)
                except (ValueError, TypeError):
                    pass
            continue
        if status == "parked":
            buckets["parked"].append(t)
            continue
        if status == "blocked":
            buckets["blocked"].append(t)
            continue
        if deadline:
            try:
                dl_dt = datetime.strptime(deadline, "%Y-%m-%d").replace(tzinfo=JST)
                hours_until = (dl_dt - now_jst).total_seconds() / 3600
                if hours_until <= 72:
                    buckets["deadlines_72h"].append(t)
            except ValueError:
                pass
        if t.get("start_hour") is not None and deadline == today_jst:
            buckets["today"].append(t)
        elif deadline == today_jst:
            buckets["today"].append(t)
        else:
            buckets["backlog"].append(t)
        last_touched = t.get("last_touched")
        if last_touched:
            try:
                dt = datetime.fromisoformat(last_touched.replace("Z", "+00:00"))
                if (now_jst - dt.astimezone(JST)).days >= 7:
                    buckets["stale"].append(t)
            except (ValueError, TypeError):
                pass
    buckets["deadlines_72h"].sort(key=lambda t: t.get("deadline_jst") or "9999")
    buckets["today"].sort(key=lambda t: t.get("start_hour") or 99)
    buckets["shipped_today"].sort(key=lambda t: t.get("completed_at") or "")
    return buckets


def main():
    events = load_events()
    tasks = fold(events)
    buckets = bucket(tasks)
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generated_at_jst": datetime.now(JST).isoformat(),
        "today_jst": datetime.now(JST).strftime("%Y-%m-%d"),
        "event_count": len(events),
        "task_count": len(tasks),
        "tasks": tasks,
        "buckets": buckets,
    }
    if "--dry-run" in sys.argv:
        print(json.dumps(out, indent=2, default=str))
        return
    with open(JSON_OUT, "w") as f:
        json.dump(out, f, indent=2, default=str)
    # Also emit window-scoped JS for file:// dashboard (fetch blocked on file://).
    with open(JS_OUT, "w") as f:
        f.write("window.TASKS_STATE = ")
        json.dump(out, f, default=str)
        f.write(";\n")
    print(f"Derived {len(tasks)} tasks from {len(events)} events -> {JSON_OUT} + {JS_OUT}")


if __name__ == "__main__":
    main()
