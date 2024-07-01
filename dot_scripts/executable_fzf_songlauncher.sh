#! /bin/sh

#DOC#@CLI@ "Play a song with cmus (chose it with fzf)"

cmus-remote -f "$(find -L music -type f | fzf)"
