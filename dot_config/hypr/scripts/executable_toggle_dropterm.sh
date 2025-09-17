#!/usr/bin/env bash
set -euo pipefail

TITLE="dropdown-term"
SPECIAL="term"

# Pick a terminal (prefer kitty, then alacritty, then foot)
if command -v alacritty >/dev/null 2>&1; then
  TERM_CMD=(alacritty --class "$TITLE" -T "$TITLE")
elif command -v kitty >/dev/null 2>&1; then
  TERM_CMD=(kitty --title "$TITLE")
elif command -v foot >/dev/null 2>&1; then
  TERM_CMD=(foot --app-id "$TITLE" --title "$TITLE")
else
  echo "No supported terminal found (kitty/alacritty/foot)." >&2
  exit 1
fi

# If a dropdown already exists (matched by title), just toggle the special workspace.
if hyprctl clients | grep -q "title: $TITLE"; then
  hyprctl dispatch togglespecialworkspace "$SPECIAL"
  exit 0
fi

# Otherwise, spawn it into the special workspace and then toggle to show it.
hyprctl dispatch exec "[workspace special:$SPECIAL] ${TERM_CMD[*]}"

# Give Hyprland a moment to register the new client, then toggle.
sleep 0.05
hyprctl dispatch togglespecialworkspace "$SPECIAL"
