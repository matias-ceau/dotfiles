#! /usr/bin/env bash

#DOC#=2024-06= "Similar to dmenu but with fzf and urxvt (this is only hte helper function"

xterm -T 'fzfmenu' -e  bash -c "fzf $* < /proc/$$/fd/0 > /proc/$$/fd/1"
