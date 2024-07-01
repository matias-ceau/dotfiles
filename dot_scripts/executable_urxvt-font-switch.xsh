#! /usr/bin/xonsh

#DOC#@RUN@ "Switch Xressources file with alternative one"

mv ~/.Xresources ~/.XresourcesTEMP
mv ~/.Xresources-alternative ~/.Xresources
mv ~/.XresourcesTEMP ~/.Xresources-alternative
xrdb ~/.Xresources

