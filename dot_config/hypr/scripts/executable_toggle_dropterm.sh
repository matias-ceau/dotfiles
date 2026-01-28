#!/usr/bin/env bash
set -euo pipefail

TITLE="dropdown-term"
SPECIAL="term"

# Ensure dropdown geometry even if rules miss (fallback)
ensure_geometry() {
  local addr mon x0 y0 mw mh x y w h floating

  # 1) Try to find by exact title via JSON if jq exists
  if command -v jq >/dev/null 2>&1; then
    addr=$(hyprctl clients -j | jq -r '.[] | select(.title=="'"$TITLE"'") | .address' | head -n1)
  fi

  # 2) If not found, try plaintext parse: pick client on special:term from known terminal classes
  if [ -z "${addr:-}" ]; then
    addr=$(hyprctl clients | awk -v RS="" -v ORS="\n\n" -v t1="(special:term)" -v classes="(Alacritty|kitty|foot)" '
      match($0, /^Window ([0-9a-fx]+) ->/, m) {
        header=m[0]; addr=m[1]
        if ($0 ~ /workspace: .* \(special:term\)/ && $0 ~ /class: (Alacritty|kitty|foot)/) {
          print addr; exit
        }
      }')
  fi

  [ -z "${addr:-}" ] && return 0

  # Focus the window to target dispatches
  hyprctl dispatch focuswindow "address:$addr" >/dev/null 2>&1 || true

  # Determine monitor and its geometry
  if command -v jq >/dev/null 2>&1; then
    floating=$(hyprctl clients -j | jq -r '.[] | select(.address=="'"$addr"'") | .floating')
    mon=$(hyprctl clients -j | jq -r '.[] | select(.address=="'"$addr"'") | .monitor')
    read -r x0 y0 mw mh <<EOF
$(hyprctl monitors -j | jq -r '.['"${mon:-0}"'] | "\(.x) \(.y) \(.width) \(.height)"')
EOF
  else
    # floating flag (best effort)
    floating=$(hyprctl clients | awk -v RS="" -v a="$addr" 'index($0,a){ if ($0 ~ /\nfloating: 1/) print "true"; else print "false" }')
    # monitor index for this client
    mon=$(hyprctl clients | awk -v RS="" -v a="$addr" 'index($0,a){ match($0,/\n\tmonitor: ([0-9]+)/,m); print m[1]; exit }')
    # monitor geometry by ID
    read -r x0 y0 mw mh <<EOF
$(hyprctl monitors | awk -v RS="\n\n" -v id="${mon:-0}" 'match($0,/ID '"${mon:-0}"'/){ match($0,/\n\tx: ([0-9]+)/,mx); match($0,/\n\ty: ([0-9]+)/,my); match($0,/\n\twidth: ([0-9]+)/,mw); match($0,/\n\theight: ([0-9]+)/,mh); printf "%s %s %s %s", mx[1], my[1], mw[1], mh[1] }')
EOF
  fi

  # Ensure floating
  if [ "$floating" != "true" ]; then
    hyprctl dispatch togglefloating >/dev/null 2>&1 || true
  fi

  # Compute target: 98% width, 60% height, x=1% (center), y=22px (below waybar)
  read -r x y w h <<EOF
$(awk -v x0="${x0:-0}" -v y0="${y0:-0}" -v mw="${mw:-0}" -v mh="${mh:-0}" 'BEGIN{w=int(mw*0.98);h=int(mh*0.60);x=int(x0+mw*0.01);y=int(y0+22);printf "%d %d %d %d", x,y,w,h }')
EOF

  hyprctl dispatch movewindowpixel "exact $x $y, address:$addr" >/dev/null 2>&1 || true
  hyprctl dispatch resizewindowpixel "exact $w $h, address:$addr" >/dev/null 2>&1 || true
}

# Pick a terminal (prefer kitty, then alacritty, then foot)
if command -v alacritty >/dev/null 2>&1; then
  TERM_CMD=(alacritty --class "$TITLE" -T "$TITLE")
elif command -v kitty >/dev/null 2>&1; then
  TERM_CMD=(kitty --title "$TITLE")
elif command -v foot >/dev/null 2>&1; then
  TERM_CMD=(foot --app-id "$TITLE" --title "$TITLE")
else
  echo "No supported terminal found (alacritty/kitty/foot)." >&2
  exit 1
fi

get_client_json() {
  hyprctl clients -j | jq -r '.[] | select(.title=="'"$TITLE"'")'
}

# If a dropdown already exists, toggle based on visibility.
if command -v jq >/dev/null 2>&1; then
  existing=$(get_client_json || true)
  if [ -n "$existing" ]; then
    hidden=$(printf '%s' "$existing" | jq -r '.hidden')
    if [ "$hidden" = "true" ]; then
      # It is hidden; show it, focus it, then enforce geometry.
      hyprctl dispatch togglespecialworkspace "$SPECIAL"
      sleep 0.05
      addr=$(printf '%s' "$existing" | jq -r '.address')
      hyprctl dispatch focuswindow "address:$addr" >/dev/null 2>&1 || true
      sleep 0.03
      ensure_geometry
    else
      # It is visible; hide it. Do not touch geometry to avoid re-showing.
      hyprctl dispatch togglespecialworkspace "$SPECIAL"
    fi
    exit 0
  fi
else
  # Fallback without jq: naive toggle if title present
  if hyprctl clients | grep -q "title: $TITLE"; then
    hyprctl dispatch togglespecialworkspace "$SPECIAL"
    exit 0
  fi
fi

# Otherwise, spawn it into the special workspace and then toggle to show it.
hyprctl dispatch exec "[workspace special:$SPECIAL] ${TERM_CMD[*]}"

# Give Hyprland a moment to register the new client, then toggle.
sleep 0.05
hyprctl dispatch togglespecialworkspace "$SPECIAL"

# Enforce geometry after showing
sleep 0.08
# Explicit final focus to ensure dropdown is active
if command -v jq >/dev/null 2>&1; then
  addr=$(hyprctl clients -j | jq -r '.[] | select(.title=="'"$TITLE"'") | .address' | head -n1)
  [ -n "$addr" ] && hyprctl dispatch focuswindow "address:$addr" >/dev/null 2>&1 || true
fi
ensure_geometry
