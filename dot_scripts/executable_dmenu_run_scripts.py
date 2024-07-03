#! /usr/bin/python

#DOC#=2024-06=$in_progress$@CLI@ "A sort of dmenu_run??"

import subprocess

# Get the choices from script_identifier.xsh
choices = subprocess.run(
    ['xonsh', 'script_identifier.xsh', '-c', 'TYPE=RUN', 'HOST', 'STATUS=active', 'OK', '-f', '"<span color=\'green\'>{FILE:<30}</span> \u27F6   {DESCR}"', '-s', 'FILE'],
    capture_output=True, text=True
).stdout

# Use rofi to select from choices
rofi_output = subprocess.run(
    ['rofi', '-dmenu', '-markup-rows', '-i', '-lines', '30', '-width', '80'],
    input=choices, capture_output=True, text=True
).stdout

# Extract the choice
choice = rofi_output.split('>')[1].split('<')[0].strip()

# Execute the selected choice
subprocess.run([choice])
