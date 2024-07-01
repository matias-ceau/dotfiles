#! /bin/sh

#DOC#@RUN@ "Pick any pdf in home folder and open it with evince"

file=$(find ~ 2>/dev/null | grep "\.pdf$" | dmenu -i -l 30)
evince "$file"
