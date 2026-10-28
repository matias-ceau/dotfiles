#!/usr/bin/env bash
set -euo pipefail

# Usage: resize_floating.sh <dx> <dy>
dx=${1:-0}
dy=${2:-0}

# Only resize when the active window is floating (Qtile-like behavior)
if hyprctl activewindow -j | grep -q '"floating": true'; then
  hyprctl dispatch "hl.dsp.window.resize({ x = $dx, y = $dy, relative = true })"
  # Recenter after resizing so it grows/shrinks evenly
  hyprctl dispatch "hl.dsp.window.center()"
fi

