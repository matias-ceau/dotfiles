#!/usr/bin/env bash
set -euo pipefail

TITLE="foot-tmux"
SPECIAL="tmux"

# Prefer footclient, then foot; fall back to kitty/alacritty
if command -v footclient >/dev/null 2>&1; then
  TERM_CMD=(footclient --app-id "$TITLE" --title "$TITLE" sh -lc 'tmux attach || tmux')
elif command -v foot >/dev/null 2>&1; then
  TERM_CMD=(foot --app-id "$TITLE" --title "$TITLE" sh -lc 'tmux attach || tmux')
elif command -v kitty >/dev/null 2>&1; then
  TERM_CMD=(kitty --title "$TITLE" sh -lc 'tmux attach || tmux')
elif command -v alacritty >/dev/null 2>&1; then
  TERM_CMD=(alacritty --class "$TITLE" -T "$TITLE" -e sh -lc 'tmux attach || tmux')
else
  echo "No supported terminal found (footclient/foot/kitty/alacritty)." >&2
  exit 1
fi

if command -v jq >/dev/null 2>&1; then
  existing=$(hyprctl clients -j | jq -r '.[] | select(.title=="'"$TITLE"'")')
  if [ -n "$existing" ]; then
    hidden=$(printf '%s' "$existing" | jq -r '.hidden')
    addr=$(printf '%s' "$existing" | jq -r '.address')
    if [ "$hidden" = "true" ]; then
      hyprctl dispatch togglespecialworkspace "$SPECIAL"
      sleep 0.08
      [ -n "$addr" ] && hyprctl dispatch focuswindow "address:$addr" >/dev/null 2>&1 || true
    else
      hyprctl dispatch togglespecialworkspace "$SPECIAL"
    fi
    exit 0
  fi
else
  if hyprctl clients | grep -q "title: $TITLE"; then
    hyprctl dispatch togglespecialworkspace "$SPECIAL"
    exit 0
  fi
fi

# Spawn on the special workspace, then toggle to show it and focus
hyprctl dispatch exec "[workspace special:$SPECIAL] ${TERM_CMD[*]}"
sleep 0.06
hyprctl dispatch togglespecialworkspace "$SPECIAL"
sleep 0.06
if command -v jq >/dev/null 2>&1; then
  addr=$(hyprctl clients -j | jq -r '.[] | select(.title=="'"$TITLE"'") | .address' | head -n1)
  [ -n "$addr" ] && hyprctl dispatch focuswindow "address:$addr" >/dev/null 2>&1 || true
fi

