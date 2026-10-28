#!/usr/bin/env bash
set -euo pipefail

SPECIAL="ai"
TITLE="chatbot"

if command -v alacritty >/dev/null 2>&1; then
  TERM_CMD=(alacritty -T "$TITLE" -e aichat)
elif command -v kitty >/dev/null 2>&1; then
  TERM_CMD=(kitty --title "$TITLE" aichat)
else
  echo "No supported terminal found (alacritty/kitty)." >&2
  exit 1
fi

# If a chatbot window exists, toggle special workspace
if hyprctl clients | grep -q "title: $TITLE"; then
  hyprctl dispatch "hl.dsp.workspace.toggle_special(\"$SPECIAL\")"
  exit 0
fi

# Spawn it into the special workspace and then toggle.
hyprctl dispatch "hl.dsp.exec_cmd([==[${TERM_CMD[*]}]==], { workspace = \"special:$SPECIAL\" })"
sleep 0.05
hyprctl dispatch "hl.dsp.workspace.toggle_special(\"$SPECIAL\")"
