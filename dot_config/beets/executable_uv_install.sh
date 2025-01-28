#!/usr/bin/bash

uv tool install git+https://github.com/beetbox/beets \
	-p 3.13 \
	--with pyacoustid \
	--with python3-discogs-client \
	--with pylast \
	--with requests \
	--with python-mpd2 \
	--with typing_extensions \
	--with git+https://github.com/adamjakab/BeetsPluginXtractor

# cd `uv tool dir` || exit
# cd beets || exit
# uv pip install \
beet
