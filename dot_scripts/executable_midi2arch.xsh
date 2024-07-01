#!/usr/bin/env xonsh

#DOC#@RUN@~karjala~ "Transform a midi controller to a keyboard/script launcher"

# Author Matias Ceau (2024) (Inspired by Author Fippls, 2019)

import subprocess
import yaml
import os
from xonsh.lexer import Lexer
#########################
cfg_path = os.path.expanduser('~/.scripts/config/midi2arch/nanoKONTROL2.yaml')
with open(cfg_path,'r') as f:
    CFG = yaml.safe_load(f) 


print(f"Midi Arch Control (inspired by Fippls industries inc.)\n")

if len($ARGS) > 0 and $ARGS[0] == "-h":
    print("Usage: $0 [-l]")
    print("   -l List events only (no output)")
    exit(1)

# Detect which device to use, in order of priority
# -------------------
def detect_midi_keyboard(keyboard):
    return $(aseqdump -l | grep @(keyboard) | wc -l)

if detect_midi_keyboard("nanoKONTROL2") != 0:
    print("Found nanoKONTROL2!")
    DEVICE = "nanoKONTROL2"
else:
    print("Found no supported MIDI devices!")
    exit(1)

# -------------------

if len($ARGS) > 0 and $ARGS[0] == "-l":
    print("Dumping events only, no keypresses will be reported")
    aseqdump -p @(DEVICE)
    exit(0)

#def trigger_key(key):
#    print(f"Triggering {key}")
#    xdotool key @(key)

# Translates a note into a keypress signal
#def translate_note(note):
#    if DEVICE == "MPK mini":
#        match note:
#            case "48":
#                trigger_key("ctrl+alt+1")
#                trigger_key("ctrl+F3")

#aseqdump -p @(DEVICE) | while read line:
#    parts = line.split()
#    if len(parts) < 4:
#        continue
#    ev1, ev2, data1 = parts[1], parts[2], parts[5]
#    if ev1 == "Note" and ev2 == "on":
#        translate_note(data1)


## IN THE FUTURE, CONSIDER USING
#for line in !(aseqdump -p "nanoKONTROL2").itercheck():
#    print(line) 

def main(config_file):
    device = config_file['general']['name']
    controls = config_file['controls']
    process = subprocess.Popen(['aseqdump','-p',device],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
    while True:
        output = process.stdout.readline()
        if output:
            try:
                cc = int(output.split(',')[1].split(' ')[-1])
                val = int(output.split(',')[-1].split(' ')[-1])
                print(cc,val)
                if cc == 39:
                    process.terminate()
                    process.wait()
                    print("Bye")
                    break
                if val == 127:
                    ctrl = {k : (a,c,d) for k,(a,b,c,d) in controls.items() if int(b) == cc}
                    cmd = list(ctrl.values())[-1][-1]
                    print(cmd)
                    @(cmd)
            except Exception as e:
                print(e)

main(CFG)
