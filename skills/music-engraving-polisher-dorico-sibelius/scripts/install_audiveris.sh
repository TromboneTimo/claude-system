#!/usr/bin/env bash
# One-time Audiveris installer (macOS). Downloads .dmg from GitHub Releases,
# mounts it, copies the app to ~/Applications, unmounts.
# Called only when user input is a PDF/image AND Audiveris isn't already
# installed. Safe to re-run, idempotent.

set -euo pipefail

APP_PATH="$HOME/Applications/Audiveris.app"
SYS_APP_PATH="/Applications/Audiveris.app"

if [ -d "$APP_PATH" ] || [ -d "$SYS_APP_PATH" ]; then
    echo "Audiveris already installed."
    exit 0
fi

echo "Audiveris not found. Installing one-time from GitHub Releases..."
echo "This will download ~100MB and copy Audiveris.app to ~/Applications."

LATEST_URL=$(curl -s https://api.github.com/repos/Audiveris/audiveris/releases/latest \
    | grep "browser_download_url.*\.dmg" \
    | head -1 \
    | cut -d '"' -f 4)

if [ -z "$LATEST_URL" ]; then
    echo "ERROR: Could not find a .dmg asset in the latest Audiveris release." >&2
    echo "Please install manually from https://github.com/Audiveris/audiveris/releases" >&2
    exit 1
fi

TMP_DMG=$(mktemp -t audiveris).dmg
echo "Downloading $LATEST_URL..."
curl -L "$LATEST_URL" -o "$TMP_DMG"

echo "Mounting dmg (auto-accepting AGPL license)..."
# Audiveris ships with a GNU AGPL license agreement that hdiutil requires
# acknowledgment for. Pipe 'yes' to auto-accept, suppress pager.
MOUNT_OUT=$(yes | PAGER=cat hdiutil attach "$TMP_DMG" -nobrowse -noverify -noautoopen 2>&1)
MOUNT_POINT=$(echo "$MOUNT_OUT" | grep "/Volumes/" | tail -1 | awk '{print $NF}')

if [ -z "$MOUNT_POINT" ] || [ ! -d "$MOUNT_POINT" ]; then
    echo "ERROR: Could not mount Audiveris dmg." >&2
    rm -f "$TMP_DMG"
    exit 1
fi

echo "Copying Audiveris.app to ~/Applications..."
mkdir -p "$HOME/Applications"
cp -R "$MOUNT_POINT/Audiveris.app" "$HOME/Applications/"

echo "Unmounting..."
hdiutil detach "$MOUNT_POINT" -quiet
rm -f "$TMP_DMG"

if [ -d "$APP_PATH" ]; then
    echo "Audiveris installed at $APP_PATH"
else
    echo "ERROR: Install appears to have failed. Check $HOME/Applications." >&2
    exit 1
fi