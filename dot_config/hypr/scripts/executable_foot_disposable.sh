#!/usr/bin/env bash
set -euo pipefail

TITLE="foot-disposable"

# Prefer footclient, then foot, then kitty/alacritty as fallback
if command -v footclient >/dev/null 2>&1; then
  TERM_CMD=(footclient --app-id "$TITLE" --title "$TITLE")
elif command -v foot >/dev/null 2>&1; then
  TERM_CMD=(foot --app-id "$TITLE" --title "$TITLE")
elif command -v kitty >/dev/null 2>&1; then
  TERM_CMD=(kitty --title "$TITLE")
elif command -v alacritty >/dev/null 2>&1; then
  TERM_CMD=(alacritty --class "$TITLE" -T "$TITLE")
else
  echo "No supported terminal found (footclient/foot/kitty/alacritty)." >&2
  exit 1
fi

# Spawn it; rules will ensure floating. Focus will raise above others.
hyprctl dispatch exec "${TERM_CMD[*]}" >/dev/null 2>&1 || true

# Try to focus by title (brings it to the top of floating stack)
sleep 0.05
if command -v jq >/dev/null 2>&1; then
  addr=$(hyprctl clients -j | jq -r '.[] | select(.title=="'"$TITLE"'") | .address' | head -n1)
  if [ -n "$addr" ]; then
    hyprctl dispatch focuswindow "address:$addr" >/dev/null 2>&1 || true
  fi
fi

