#! /usr/bin/env xonsh

#DOC#@CLI@ "Choose an album with fzf and play it with cmus"

selection=$(beet ls -a | sed 's/.* - //g' | fzf).strip()
if selection:
    cmus-remote -C 'view 4'
    cmus-remote -C clear
    cmus-remote -C 'view 2'
    query=f'filter album="{selection}"'
    cmus-remote -C @(query)
    cmus-remote -C mark
    cmus-remote -C win-add-q
    cmus-remote -C filter
    cmus-remote -C 'view 4'
    cmus-remote -C "lqueue 100"
    cmus-remote -n
    cmus-remote -p
    cmus-remote -C "save /home/matias/.temp/nowplaying.m3u"

