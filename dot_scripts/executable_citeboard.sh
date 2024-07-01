#! /bin/sh

#DOC#@RUN@ "Find a paper and either open the paper or copy the paper citation"
#+needed+ findutils xsel dmenu

ref=$(grep -h "^@" data/bib/* | grep ,$ | sed 's/@.*{//g ; s/,$//g' | dmenu -l 30 | sed 's/\n$//g')

sel=$(echo -e "open\nclipboard" | dmenu)

[ "$ref" = "" ] && exit 
[ "$sel" = "clipboard" ] && echo "$ref" | xsel -b
[ "$sel" = "open" ] && 
    find data/zotero/storage | grep "$ref" | xargs evince
