#!/bin/bash

# Function to check if a command exists and start it, otherwise log an error

start_if_exists() {
    if command -v "$1" &>/dev/null; then
        "$@" &
    else
        logger "Error: $1 not found"
    fi
}

#~/.fehbg &
start_if_exists nm-applet
#start_if_exists dropbox #already with autostart
# start_if_exists flameshot
start_if_exists dunst
start_if_exists swww-daemon
# start_if_exists picom -b
start_if_exists tmux_manager.py --auto
#start_if_exists /usr/bin/emacs --daemon
#start_if_exists /usr/bin/xonsh ~/scripts/karjala_screen.xsh
start_if_exist systemd run --scope --user internxt webdav enable
