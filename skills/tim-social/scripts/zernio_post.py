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
import time

ZSHRC = os.path.expanduser("~/.zshrc")
BASE = "https://zernio.com/api/v1"
UA = "Mozilla/5.0 (creator-conservatory tim-social post)"
RETRIES = 3


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

    # Reddit-specific settings
    if args.platform == "reddit":
        if not args.subreddit:
            sys.exit("--subreddit required for reddit posts")
        body["redditSettings"] = {
            "subreddit": args.subreddit,
            "title": args.title or args.content.split("\n", 1)[0][:300],
        }
        if args.flair_id:
            body["redditSettings"]["flairId"] = args.flair_id
        if args.url:
            body["redditSettings"]["url"] = args.url
        body["redditSettings"]["forceSelf"] = args.force_self

    # Twitter/X thread support
    if args.platform == "twitter" and args.thread_items:
        body["twitterSettings"] = {"threadItems": json.loads(args.thread_items)}

    return body


def post(body, key):
    """POST with retry-with-backoff for transient connection resets."""
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
    last_err = None
    for attempt in range(RETRIES):
        try:
            out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=35).decode()
            body_text, _, code = out.rpartition("__HTTP__")
            code_int = int(code or 0)
            # Retry only on connection resets (code=0) or 5xx; not on 4xx (client error, our fault)
            if code_int == 0 or 500 <= code_int < 600:
                last_err = f"HTTP {code_int}: {body_text.strip()[:200]}"
                if attempt < RETRIES - 1:
                    time.sleep(2 ** attempt)
                    continue
            return body_text.strip(), code_int
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            last_err = str(e)[:200]
            if attempt < RETRIES - 1:
                time.sleep(2 ** attempt)
                continue
    return f'{{"error":"all_retries_failed","detail":"{last_err}"}}', 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--platform", required=True, choices=["facebook", "linkedin", "youtube", "tiktok", "instagram", "twitter", "reddit"])
    p.add_argument("--account-id", required=True)
    p.add_argument("--content", required=True)
    p.add_argument("--mode", required=True, choices=["draft", "publish", "schedule"])
    p.add_argument("--scheduled-for", default=None)
    p.add_argument("--media-url", default=None)
    p.add_argument("--media-type", default="image", choices=["image", "video"])
    # Reddit-specific
    p.add_argument("--subreddit", default=None, help="Reddit only: target subreddit name without r/")
    p.add_argument("--title", default=None, help="Reddit only: post title (max 300 chars). Defaults to first line of content.")
    p.add_argument("--flair-id", default=None, help="Reddit only: flair ID if subreddit requires one")
    p.add_argument("--url", default=None, help="Reddit only: URL for link posts")
    p.add_argument("--force-self", action="store_true", help="Reddit only: force text/self post even if URL provided")
    # Twitter-specific
    p.add_argument("--thread-items", default=None, help="Twitter only: JSON-encoded array of follow-up tweets for threads")
    # Safety
    p.add_argument("--dry-run", action="store_true", help="Print the request body that WOULD be sent. No API call. Always run this before --mode publish on a real account.")
    args = p.parse_args()

    body = build_body(args)

    if args.dry_run:
        print(json.dumps({"dry_run": True, "platform": args.platform, "mode": args.mode, "body": body}, indent=2))
        sys.exit(0)

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
