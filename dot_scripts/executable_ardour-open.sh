#! /bin/sh

#DOC#@RUN@ "Open an ardour session"

session="$(find /home/matias/audio/PROJECTS | grep "\.ardour$" | sed 's/\/home\/matias\/audio\/PROJECTS//' | dmenu -i -l 30)"
ardour "/home/matias/audio/PROJECTS/$session"
