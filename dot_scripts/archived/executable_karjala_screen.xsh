#! /usr/bin/env xonsh

#DOC#@RUN@~karjala~$deprecated$ "Old double screen xrandr command"

if $(cat /etc/hostname).splitlines()[0] == 'karjala':
    xrandr --output DVI-D-0 --off --output HDMI-0 --primary --mode 1360x768 --pos 1360x0 --rotate normal --output HDMI-1 --mode 1360x768 --pos 0x0 --rotate normal --output DP-0 --off --output DP-1 --off --output DP-2 --off --output DP-3 --off
