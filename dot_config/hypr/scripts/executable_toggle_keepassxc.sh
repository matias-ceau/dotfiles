#!/usr/bin/env bash
set -euo pipefail

SPECIAL="kp"

# Unlock the KeePassXC database using the master password from pass.
KP_CMD="pass lavomatyc show | keepassxc --keyfile ${HOME}/Documents/georgeabitbol --pw-stdin ${HOME}/.localdata/monkeypass/database.kdbx"
KP_CLASS_RE="^(KeePassXC|keepassxc|org\\.keepassxc\\.KeePassXC)$"

PP_CMD="proton-pass"
PP_CLASS_RE="^(proton-pass|Proton Pass)$"

MODE="toggle"
if [[ "${1:-}" == "--ensure" ]]; then
  MODE="ensure"
fi

has_client() {
  local class_re="$1"
  hyprctl clients | grep -Eq "(class|app): .*${class_re}"
}

move_to_special_if_present() {
  local class_re="$1"
  hyprctl dispatch movetoworkspacesilent "special:${SPECIAL},class:${class_re}" || true
}

ensure_app() {
  local class_re="$1" cmd="$2"
  if has_client "${class_re}"; then
    move_to_special_if_present "${class_re}"
    return 0
  fi

  if [[ "$MODE" == "ensure" ]]; then
    return 0
  fi

  hyprctl dispatch exec "[workspace special:${SPECIAL}] ${cmd}"
}

ensure_app "${KP_CLASS_RE}" "${KP_CMD}"
ensure_app "${PP_CLASS_RE}" "${PP_CMD}"

sleep 0.1

if [[ "$MODE" == "toggle" ]]; then
  hyprctl dispatch togglespecialworkspace "$SPECIAL"
fi
