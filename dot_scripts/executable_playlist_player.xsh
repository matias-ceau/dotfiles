#! /usr/bin/env xonsh

#DOC#@RUN@ "Pick a playlist and play it"

import os
PLAYLIST_PATH = os.path.expanduser('~/.playlists') 

cmus-remote -C 'view 4'
cmus-remote -C clear
options = '\n'.join(sorted([i.split('.')[0] for i in os.listdir(PLAYLIST_PATH) if 'm3u' in i]))
choice = $(echo @(options) | dmenu -i -l 30).strip()
cmus-remote -C @(f'add {PLAYLIST_PATH}/{choice}.m3u')
cmus-remote -n
cmus-remote -p
