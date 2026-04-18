#!/usr/bin/env python3
"""/task CLI. Mutates tasks.jsonl, runs derive, returns a human confirmation.

Subcommands:
  add "<title>" [--deadline YYYY-MM-DD] [--tier T1|T2|T3] [--project <name>]
                [--est 30] [--start 14] [--tags a,b]
  done <id|partial-title> [--shipped "note"]
  list [--status active|blocked|parked|completed]
  today
  park <id|partial-title>
  block <id|partial-title> --on "waiting for X"
  start <id|partial-title>

Called from the /task slash command (see SKILL.md). Writes only via append.
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.home() / ".claude"
STATE = ROOT / "state"
JSONL = STATE / "tasks.jsonl"
JSON = STATE / "tasks.json"
DERIVE = STATE / "derive.py"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slugify(s, existing_ids):
    base = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40] or "task"
    cand = base
    n = 2
    while cand in existing_ids:
        cand = f"{base}-{n}"
        n += 1
    return cand


def append_event(ev):
    STATE.mkdir(parents=True, exist_ok=True)
    with open(JSONL, "a") as f:
        f.write(json.dumps(ev) + "\n")


def load_tasks():
    if not JSON.exists():
        run_derive()
    with open(JSON) as f:
        return json.load(f)


def run_derive():
    subprocess.run(["python3", str(DERIVE)], check=True, capture_output=True)


def resolve_id(query, state, allow_status=None):
    """Match exact id first, then substring on title."""
    tasks = state.get("tasks", {})
    if query in tasks:
        return query
    q = query.lower()
    matches = []
    for tid, t in tasks.items():
        if allow_status and t.get("status") not in allow_status:
            continue
        if q in tid.lower() or q in (t.get("title") or "").lower():
            matches.append((tid, t))
    if not matches:
        return None
    if len(matches) == 1:
        return matches[0][0]
    # Prefer exact title word match
    for tid, t in matches:
        if q in re.split(r"\W+", (t.get("title") or "").lower()):
            return tid
    print(f"ambiguous query '{query}'. candidates:", file=sys.stderr)
    for tid, t in matches[:5]:
        print(f"  {tid}: {t.get('title', '')[:70]}", file=sys.stderr)
    return None


def cmd_add(args):
    state = load_tasks() if JSONL.exists() else {"tasks": {}}
    existing = set(state.get("tasks", {}).keys())
    tid = slugify(args.title, existing)
    tags = [t.strip() for t in (args.tags or "").split(",") if t.strip()]
    ev = {
        "event": "task.created",
        "id": tid,
        "ts": now_iso(),
        "title": args.title,
        "project": args.project or "",
        "tier": args.tier or "T2",
    }
    if args.deadline:
        ev["deadline_jst"] = args.deadline
    if args.est is not None:
        ev["estimated_min"] = args.est
    if args.start is not None:
        ev["start_hour"] = args.start
    if tags:
        ev["tags"] = tags
    append_event(ev)
    run_derive()
    msg = f"added [{tid}] {args.title}"
    bits = []
    if args.tier: bits.append(args.tier)
    if args.deadline: bits.append(f"due {args.deadline}")
    if args.start is not None: bits.append(f"starts {args.start:02d}:00")
    if args.est: bits.append(f"~{args.est}m")
    if bits: msg += f" ({', '.join(bits)})"
    print(msg)


def cmd_done(args):
    state = load_tasks()
    tid = resolve_id(args.query, state, allow_status={"active", "blocked"})
    if not tid:
        sys.exit(f"no active task matching '{args.query}'")
    ev = {"event": "task.completed", "id": tid, "ts": now_iso()}
    if args.shipped:
        ev["shipped"] = args.shipped
    append_event(ev)
    run_derive()
    t = state["tasks"][tid]
    print(f"DONE [{tid}] {t['title'][:70]}" + (f" ({args.shipped})" if args.shipped else ""))


def cmd_park(args):
    state = load_tasks()
    tid = resolve_id(args.query, state, allow_status={"active", "blocked"})
    if not tid:
        sys.exit(f"no task matching '{args.query}'")
    append_event({"event": "task.parked", "id": tid, "ts": now_iso()})
    run_derive()
    t = state["tasks"][tid]
    print(f"parked [{tid}] {t['title'][:70]}")


def cmd_block(args):
    state = load_tasks()
    tid = resolve_id(args.query, state, allow_status={"active"})
    if not tid:
        sys.exit(f"no active task matching '{args.query}'")
    append_event({
        "event": "task.blocked",
        "id": tid,
        "ts": now_iso(),
        "blocked_on": args.on,
    })
    run_derive()
    t = state["tasks"][tid]
    print(f"blocked [{tid}] {t['title'][:60]} on: {args.on}")


def cmd_start(args):
    state = load_tasks()
    tid = resolve_id(args.query, state, allow_status={"active", "blocked"})
    if not tid:
        sys.exit(f"no task matching '{args.query}'")
    append_event({"event": "task.started", "id": tid, "ts": now_iso()})
    run_derive()
    t = state["tasks"][tid]
    print(f"started [{tid}] {t['title'][:70]}")


def cmd_list(args):
    state = load_tasks()
    tasks = state.get("tasks", {})
    status_filter = set([args.status]) if args.status else None
    rows = []
    for tid, t in tasks.items():
        if status_filter and t.get("status") not in status_filter:
            continue
        rows.append((tid, t))
    rows.sort(key=lambda r: (
        r[1].get("status") or "zz",
        r[1].get("deadline_jst") or "9999",
    ))
    if not rows:
        print("no tasks.")
        return
    for tid, t in rows:
        dl = t.get("deadline_jst") or "  no-deadline"
        print(f"{t['status']:9s} {tid:28s} {dl:12s} [{t.get('tier','--')}] {t.get('title','')[:60]}")


def cmd_today(args):
    state = load_tasks()
    b = state.get("buckets", {})
    today = b.get("today") or []
    dl = b.get("deadlines_72h") or []
    blocked = b.get("blocked") or []
    shipped = b.get("shipped_today") or []
    print(f"{state.get('today_jst','?')} JST")
    print()
    print(f"TIMEBOX TODAY ({len(today)}):")
    if today:
        for t in today:
            sh = f" @{t['start_hour']:02d}:00" if t.get("start_hour") is not None else ""
            est = f" ~{t.get('estimated_min', '?')}m"
            print(f"  [{t['id']}] {t.get('title','')[:60]}{sh}{est}")
    else:
        print("  (nothing timeboxed for today)")
    print()
    print(f"DEADLINES UNDER 72H ({len(dl)}):")
    for t in dl[:6]:
        print(f"  {t.get('deadline_jst')}: {t.get('title','')[:60]}")
    print()
    if blocked:
        print(f"BLOCKED ({len(blocked)}):")
        for t in blocked[:5]:
            print(f"  {t.get('title','')[:50]} blocked on: {t.get('blocked_on','?')[:40]}")
        print()
    print(f"SHIPPED TODAY: {len(shipped)}")
    for t in shipped[:5]:
        print(f"  done: {t.get('title','')[:60]}")


def build_parser():
    p = argparse.ArgumentParser(prog="task", description="Task state CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("add")
    pa.add_argument("title")
    pa.add_argument("--deadline", help="YYYY-MM-DD JST")
    pa.add_argument("--tier", choices=["T1", "T2", "T3"])
    pa.add_argument("--project")
    pa.add_argument("--est", type=int, help="estimated minutes")
    pa.add_argument("--start", type=int, help="start hour JST (0-23) for timeline placement")
    pa.add_argument("--tags", help="comma-separated tags")
    pa.set_defaults(fn=cmd_add)

    pd = sub.add_parser("done")
    pd.add_argument("query", help="task id or partial title")
    pd.add_argument("--shipped", help="what shipped (one-line note)")
    pd.set_defaults(fn=cmd_done)

    pp = sub.add_parser("park")
    pp.add_argument("query")
    pp.set_defaults(fn=cmd_park)

    pb = sub.add_parser("block")
    pb.add_argument("query")
    pb.add_argument("--on", required=True, help="what's blocking")
    pb.set_defaults(fn=cmd_block)

    ps = sub.add_parser("start")
    ps.add_argument("query")
    ps.set_defaults(fn=cmd_start)

    pl = sub.add_parser("list")
    pl.add_argument("--status", choices=["active", "blocked", "parked", "completed"])
    pl.set_defaults(fn=cmd_list)

    pt = sub.add_parser("today")
    pt.set_defaults(fn=cmd_today)

    return p


if __name__ == "__main__":
    args = build_parser().parse_args()
    args.fn(args)
