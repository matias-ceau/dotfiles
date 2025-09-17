#!/usr/bin/env bash
set -euo pipefail

SPECIAL="kp"
APP="${APP:-keepassxc}"
# Be liberal with identifiers so it works for Wayland/Xwayland
CLASS_REGEX="${CLASS_REGEX:-^(KeePassXC|keepassxc|org\.keepassxc\.KeePassXC)$}"

# Modes:
#  - default: toggle behavior (spawn or show/hide)
#  - --ensure: if running, move it to special workspace without toggling; do not spawn
MODE="toggle"
if [[ "${1:-}" == "--ensure" ]]; then
  MODE="ensure"
fi

has_client() {
  # Match by class/app field in `hyprctl clients` output
  hyprctl clients | grep -E "(class|app): .*${CLASS_REGEX%$}" -q
}

move_to_special_if_present() {
  # Move any matching client to the special workspace, silently
  hyprctl dispatch movetoworkspacesilent "special:${SPECIAL},class:${CLASS_REGEX}" || true
}

if has_client; then
  move_to_special_if_present
  if [[ "$MODE" == "toggle" ]]; then
    hyprctl dispatch togglespecialworkspace "$SPECIAL"
  fi
  exit 0
fi

if [[ "$MODE" == "ensure" ]]; then
  # Do not spawn in ensure mode; just exit quietly
  exit 0
fi

# Otherwise spawn it on the special workspace and toggle to show it.
hyprctl dispatch exec "[workspace special:${SPECIAL}] ${APP}"
sleep 0.05
hyprctl dispatch togglespecialworkspace "$SPECIAL"
