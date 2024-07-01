#! /bin/sh

#DOC#@RUN@ "Create a covert art based on file spectrogram"
#+needed+sox dmenu imagemagick

file="$(find /home/matias/audio/PROJECTS | grep .wav | dmenu -l 30)" 
name="$(printf $file | sed 's/.wav//')"
sox $file -n spectrogram -x 1600 -Y 900 -r -o "$name".png
convert "$name".png -resize 1600x900! "$name"_RESIZED.png
rm "$name".png
