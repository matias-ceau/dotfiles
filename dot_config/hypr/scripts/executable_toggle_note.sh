#!/usr/bin/env bash
set -euo pipefail

SPECIAL="quick"
TITLE="note"
FILE="$HOME/notes/draft.md"

# Ensure file exists
mkdir -p "$(dirname "$FILE")"
touch "$FILE"

if command -v alacritty >/dev/null 2>&1; then
  TERM_CMD=(alacritty -T "$TITLE" -e nvim "$FILE")
elif command -v kitty >/dev/null 2>&1; then
  TERM_CMD=(kitty --title "$TITLE" nvim "$FILE")
else
  echo "No supported terminal found (alacritty/kitty)." >&2
  exit 1
fi

# If a note window exists, toggle special workspace
if hyprctl clients | grep -q "title: $TITLE"; then
  hyprctl dispatch togglespecialworkspace "$SPECIAL"
  exit 0
fi

# Spawn it into the special workspace and then toggle.
hyprctl dispatch exec "[workspace special:$SPECIAL] ${TERM_CMD[*]}"
sleep 0.05
hyprctl dispatch togglespecialworkspace "$SPECIAL"

