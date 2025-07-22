import os
import subprocess

from libqtile import hook

__all__ = ["autostart", "reset_wallpaper"]


@hook.subscribe.startup_once
def autostart():
    auto = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([auto])


@hook.subscribe.startup
def reset_wallpaper():
    wall = os.path.expanduser("~/.local/bin/wallpaper.sh")
    subprocess.Popen([wall])
