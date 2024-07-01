#! /usr/bin/env xonsh

#DOC#@RUN@ "Pick a playlist of albums and play in random order in cmus"

import pandas as pd
import random
import os


PLAYLIST_PATH = os.path.expanduser('~/.playlists') 

options = '\n'.join([i.split('.')[0] for i in $(ls @PLAYLIST_PATH).split('\n') if 'm3u' in i])
selected = $(echo @(options) | dmenu -i -l 30).replace('\n','')
print(selected)
content = $(cat @(f'/home/matias/notes/playlists/{selected}.m3u')).splitlines()
content = [i for i in content if i]
albums = [i.split('/')[-2] for i in content]
songs = [i.split('/')[-1] for i in content]
df = pd.DataFrame({'albums'  : albums,
                   'songs'   : songs,
                   'content' : content})
indiv_albums = df.albums.unique().tolist()
random.shuffle(indiv_albums)
mapping = {k:v for v,k in enumerate(indiv_albums)}
df['order'] = [mapping[i] for i in df.albums]
df = df.sort_values(['order', 'songs'])
random_pl = '\n'.join(df.content.tolist())
echo @(random_pl) > /home/matias/.temp/randomized.m3u

cmus-remote -C 'view 4'
cmus-remote -C clear
cmus-remote -C 'add /home/matias/.temp/randomized.m3u'
cmus-remote -n
cmus-remote -p

