#! /usr/bin/env xonsh

#DOC#@RUN@ "Pick random wallpaper from wallpaper list"

import os
import random

folder = '/home/matias/./wallpapers'
wallpapers = [i for i in os.listdir(folder) if i[-3:]=='png' or i[-3:]=='jpg']

#selection = $(echo @('\n'.join(wallpapers)) | dmenu -i -l 30)
#if not selection:
selection = random.choice(wallpapers)

feh --bg-scale @(folder+'/'+selection.strip())
