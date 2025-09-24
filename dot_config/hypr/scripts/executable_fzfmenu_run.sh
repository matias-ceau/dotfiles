#!/usr/bin/env bash

#INFO:#@RUN@=2024-06= "Dmenu run replacement with fzf and a floating xterm terminal"

export PATH="$HOME/.local/bin:$HOME/.scripts/bin:$PATH"

# dmenu_path | improved-fzfmenu.sh | xargs -I {} bash -c "{}" &
#
cmd="$(fzfmenu_cache.sh | improved-fzfmenu.sh --pipe --ansi)"

# nothing selected -> exit
[ -z "$cmd" ] && exit 0

systemd-run --user --scope --quiet bash -c "$cmd" &
