#!/usr/bin/env python3
"""
Generic Zernio post wrapper. Used by per-platform tim-social agent skills.

Usage:
  python3 zernio_post.py --platform facebook --account-id <id> --content "..." --mode draft
  python3 zernio_post.py --platform facebook --account-id <id> --content "..." --mode publish
  python3 zernio_post.py --platform facebook --account-id <id> --content "..." --mode schedule --scheduled-for "2026-05-01T15:00:00Z"

Returns JSON to stdout: {"ok": bool, "post_id": "...", "status_code": int, "raw": {...}}
"""
import argparse
import json
import os
import re
import subprocess
import sys

ZSHRC = os.path.expanduser("~/.zshrc")
BASE = "https://zernio.com/api/v1"
UA = "Mozilla/5.0 (creator-conservatory tim-social post)"


def load_key():
    with open(ZSHRC) as f:
        m = re.search(r"sk_[a-f0-9]{64}", f.read())
    if not m:
        sys.exit("ZERNIO_API_KEY not found in ~/.zshrc")
    return m.group(0)


def build_body(args):
    body = {
        "content": args.content,
        "platforms": [{"platform": args.platform, "accountId": args.account_id}],
    }
    if args.mode == "publish":
        body["publishNow"] = True
    elif args.mode == "schedule":
        if not args.scheduled_for:
            sys.exit("--scheduled-for required for schedule mode")
        body["scheduledFor"] = args.scheduled_for
    elif args.mode == "draft":
        # Internal Zernio draft = omit both publishNow and scheduledFor.
        # For Facebook, also send platform-native draft via facebookSettings.
        if args.platform == "facebook":
            body["publishNow"] = True
            body["facebookSettings"] = {"draft": True}
        elif args.platform == "tiktok":
            body["tiktokSettings"] = {"draft": True}
    if args.media_url:
        body["mediaItems"] = [{"type": args.media_type, "url": args.media_url}]
    return body


def post(body, key):
    payload = json.dumps(body)
    cmd = [
        "curl", "-4", "-sS", "-m", "30",
        "-A", UA,
        "-H", f"Authorization: Bearer {key}",
        "-H", "Content-Type: application/json",
        "-H", "Accept: application/json",
        "-X", "POST",
        "-w", "\n__HTTP__%{http_code}",
        "--data-binary", payload,
        f"{BASE}/posts",
    ]
    out = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
    body_text, _, code = out.rpartition("__HTTP__")
    return body_text.strip(), int(code or 0)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--platform", required=True, choices=["facebook", "linkedin", "youtube", "tiktok", "instagram"])
    p.add_argument("--account-id", required=True)
    p.add_argument("--content", required=True)
    p.add_argument("--mode", required=True, choices=["draft", "publish", "schedule"])
    p.add_argument("--scheduled-for", default=None)
    p.add_argument("--media-url", default=None)
    p.add_argument("--media-type", default="image", choices=["image", "video"])
    args = p.parse_args()

    body = build_body(args)
    key = load_key()
    body_text, code = post(body, key)

    try:
        raw = json.loads(body_text)
    except json.JSONDecodeError:
        raw = {"text": body_text}

    ok = 200 <= code < 300
    post_id = raw.get("_id") or raw.get("id") or (raw.get("post") or {}).get("_id")
    print(json.dumps({"ok": ok, "post_id": post_id, "status_code": code, "raw": raw}, indent=2))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
