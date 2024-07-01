#! /bin/sh

#DOC#@RUN@$deprecated$ "used to open everything but actually useless"

search="$( find * | dmenu -l 30 )"

if [ -d $search ]; then
    cd $search
elif [ "${search##*.}" = "pdf" ]; then
    zathura $search
elif [ "${search##*.}" = "sh" ]; then
    sh $search
else
       vim $search
fi

