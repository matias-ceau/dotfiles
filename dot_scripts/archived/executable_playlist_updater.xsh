#! /usr/bin/env xonsh

#DOC#@RUN@$deprecated$ "playlist updated, note in use"

beet update -F genre
genres = [i for i in set($(beet ls -f $genre).splitlines()) if i]
genres = set([i.strip() for a in genres for i in a.split(';')])
playlists = [i for i in genres if i[0]=='0']
for p in playlists:
    tracks = '\n'.join(sorted($(beet ls -p @(f'genre:{p}')).split('\n')))
    albums = '\n'.join(sorted($(beet ls -af '$albumartist - $album' @(f'genre:{p}')).split('\n')))
    echo @(tracks) > @(f'/home/matias/notes/playlists/{p[1:]}.m3u')
    echo @(albums) > @(f'/home/matias/notes/playlists/{p[1:]}.txt')
