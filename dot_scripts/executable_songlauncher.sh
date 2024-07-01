#! /bin/sh

#DOC#@RUN@ "Play a song with cmus using dmenu"

cmus-remote -f "$(find -L music -type f | dmenu -i -l 30)"
