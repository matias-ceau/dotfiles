#! /bin/sh

#DOC#@RUN@$deprecated$ "Old script to play album with cmus"
#+required+ cmus beet

selection=$(beet ls -a | sed 's/.*\s-\s//g' | dmenu -i -l 30)
[ "$selection" != "" ] &&\
    cmus-remote -C 'view 4' &&\
    cmus-remote -C clear &&\
    cmus-remote -C 'view 2' &&\
    query="filter album=\"""$selection"\" &&\
    cmus-remote -C "$query" &&\
    cmus-remote -C mark &&\
    cmus-remote -C win-add-q &&\
    cmus-remote -C filter &&\
    cmus-remote -C 'view 4' &&\
    cmus-remote -C "lqueue 100" &&\
    cmus-remote -n &&\
    cmus-remote -p &&\
