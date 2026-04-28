#!/usr/bin/env python3
"""
Pull Zernio profiles + accounts and write them to the Tim Maines database.
Run after connecting/disconnecting any social account on zernio.com.

Usage: python3 zernio_refresh.py
"""
import json
import os
import re
import subprocess
import sys
import time

ZSHRC = os.path.expanduser("~/.zshrc")
DB = "/Users/air/Desktop/Timo LLC/creator-conservatory/tim-maines"
BASE = "https://zernio.com/api/v1"
UA = "Mozilla/5.0 (creator-conservatory tim-social refresh)"


def load_key():
    with open(ZSHRC) as f:
        m = re.search(r"sk_[a-f0-9]{64}", f.read())
    if not m:
        sys.exit("ZERNIO_API_KEY not found in ~/.zshrc")
    return m.group(0)


def fetch(path, key, retries=4):
    url = f"{BASE}{path}"
    last = None
    for attempt in range(retries):
        try:
            out = subprocess.check_output(
                [
                    "curl", "-4", "-sS", "--fail", "-m", "15",
                    "-A", UA,
                    "-H", f"Authorization: Bearer {key}",
                    "-H", "Accept: application/json",
                    url,
                ],
                stderr=subprocess.STDOUT,
            )
            return json.loads(out)
        except subprocess.CalledProcessError as e:
            last = e.output.decode(errors="replace")
            time.sleep(2 ** attempt)
        except json.JSONDecodeError as e:
            last = f"json decode: {e}"
            time.sleep(2 ** attempt)
    sys.exit(f"GET {path} failed after {retries} retries: {last}")


def main():
    key = load_key()
    profiles = fetch("/profiles", key)
    accounts = fetch("/accounts", key)

    os.makedirs(f"{DB}/config", exist_ok=True)
    with open(f"{DB}/config/zernio-profiles.json", "w") as f:
        json.dump(profiles, f, indent=2)
    with open(f"{DB}/config/zernio-accounts.json", "w") as f:
        json.dump(accounts, f, indent=2)

    print(f"profiles: {len(profiles.get('profiles', []))}")
    for p in profiles.get("profiles", []):
        print(f"  - {p['name']} ({p['_id']})")

    print(f"\naccounts: {len(accounts.get('accounts', []))}")
    by_platform = {}
    for a in accounts.get("accounts", []):
        plat = a.get("platform", "unknown")
        by_platform.setdefault(plat, []).append(a)
    for plat in ["linkedin", "youtube", "tiktok", "instagram", "facebook"]:
        accts = by_platform.get(plat, [])
        if accts:
            for a in accts:
                profname = a.get("profileId", {}).get("name", "?")
                page = a.get("metadata", {}).get("selectedPageName")
                tail = f" -> Page: {page}" if page else ""
                print(f"  [{plat:9s}] {a['username']} on {profname}{tail}")
        else:
            print(f"  [{plat:9s}] NOT CONNECTED")


if __name__ == "__main__":
    main()
