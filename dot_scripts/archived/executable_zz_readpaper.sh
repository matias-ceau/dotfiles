#! /bin/sh

#DOC#@RUN@$deprecated$ "Create note from paper"

paper="$(echo $1 | sed 's/\.pdf//g')" 
echo "$(date -I) - [$paper]($paper.md)" >> ~/notes/papers.md 
touch ~/notes/"$paper".md
echo $paper >> ~/notes/"$paper".md
echo ========== >> ~/notes/"$paper".md
echo "[$paper](resources/$paper.pdf)" >> ~/notes/"$paper".md
