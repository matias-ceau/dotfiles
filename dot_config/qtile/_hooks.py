from libqtile import hook
import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    auto = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([auto])

@hook.subscribe.startup
def reset_wallpaper():
    wall = os.path.expanduser("~/.scripts/wallpaper.sh")
    subprocess.Popen([wall])
