import sys
import spotipy
import spotipy.util as util

artistasFile = open('artistas.txt', 'r')
artista = [x.strip('\n') for x in artistasFile.readlines()]

tracks = []

numeroArtistas = len(artista)

username = 'Henrique Tardivo'
scope = 'playlist-modify-public'
playlist_id = '7hoBDz2BrOsxVhLAAph9wl'


token = util.prompt_for_user_token(username,
                                   scope,
                                   client_id='d5acc968b250491787e6caa0d99c34af',
                                   client_secret='a35a4e16369849b3bd9d5a94138e4ca3',
                                   redirect_uri='http://localhost:8080/callback')

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    for x in range(0, numeroArtistas):
        result = sp.search(artista[x], limit=4)
        for i, t in enumerate(result['tracks']['items']):
            tracks.append(str(t['id'].strip( 'u' )))
            print("adicionando a track", t['id'], t['name'])
    while tracks:
        try:
            result = sp.user_playlist_add_tracks(username, playlist_id, tracks[:1])
        except:
            print("erro")
        tracks = tracks[1:]
    
else:
    print("Can't get token for", username)