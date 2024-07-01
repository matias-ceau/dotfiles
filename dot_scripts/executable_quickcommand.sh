#! /bin/sh

#DOC#@RUN@ "Run any command with dmenu"

command=$(true | dmenu -i -p 'Sir?')
eval "$command"
