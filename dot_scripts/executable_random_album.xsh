#! /usr/bin/env xonsh

#DOC#@RUN@ "Select random album and play it with cmus"

import random
import os

temp_path = os.path.expanduser('~/.config/cmus/.temp.m3u') 

cmus-remote -U
cmus-remote -C "view 4"
cmus-remote -C clear

paths = $(cat .config/cmus/lib.pl).splitlines()
albums = list(set(['/'.join(i.split('/')[-3:-1]) for i in paths]))
random.shuffle(albums)
playlist_paths = []

for n in range(10):
    playlist_paths += [i+'\n' for i in paths if (albums[n]+'/') in i]


with open(temp_path, 'w') as f:
    f.writelines(playlist_paths)
#albums = $(beet ls -a).splitlines()
#albums = [x.split(' - ')[-1] for x in albums]
#selection = random.choice(albums)

cmus-remote -q @(temp_path)
cmus-remote -p
cmus-remote -n
