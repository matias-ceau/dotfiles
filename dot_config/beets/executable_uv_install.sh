#!/usr/bin/bash

uv tool install git+https://github.com/beetbox/beets -p 3.13
cd `uv tool dir` || exit
cd beets || exit
uv pip install \
	pyacoustid \
	python3-discogs-client \
	pylast \
	requests \
	python-mpd2 \
	typing_extensions \
	git+https://github.com/adamjakab/BeetsPluginXtractor
