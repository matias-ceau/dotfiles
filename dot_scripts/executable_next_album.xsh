#! /usr/bin/env xonsh

#DOC#@RUN@ "Skip to next album in cmus"

cmus-remote -C 'view 4'
cmus-remote -C 'save /home/matias/.temp/now_playing.m3u'
now = $(cat "/home/matias/.temp/now_playing.m3u").splitlines()
now = [i for i in now if i]
counter = 1
albums = [i.split('/')[-2] for i in now]
current_album = $(cmus-remote -Q).splitlines()[1].split('/')[-2]
for a in albums:
    if a != current_album:
        break
    counter += 1
for i in range(counter):
    cmus-remote -n
