#! /usr/bin/env xonsh

#DOC#@RUN@=2024-06= "Run user scripts with dmenu"

choices = $(script_identifier.xsh -c TYPE=RUN HOST STATUS=active OK -f "<span color='green'>{FILE:<30}</span> \u27F6   {DESCR}" -s FILE)
choice = $(echo @(choices) | rofi -dmenu -markup-rows -i -lines 30 -width 80).split('>')[1].split('<')[0].strip()
@(choice)
