import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

#variables for OAuth:
scope = "playlist-modify-public"
username = 	"esxvwcdx8i0iiqlngeilpzz8q"
redirect_uri = "http://127.0.0.1:8080/"

client_id = "1c17a15a1ddd4c55a0d611f9536a8c0e"
client_secret = "55fd17d4789c4811995a1cc37ee8d0de"

token = SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, username=username)

#starting the Spotify object.
spotifyObject = spotipy.Spotify(auth_manager=token)

#create a playlist
playlistName = input("What artist is this playlist on? ")
playlistDesc = input("Give your playlist a description: ")

spotifyObject.user_playlist_create(user=username, public=True, name=playlistName, description=playlistDesc)

#get songs to add
result = spotifyObject.search(q=playlistName)
artistURI = result['tracks']['items'][0]['artists'][0]['uri']

artistSongs = []
songs = spotifyObject.artist_top_tracks(artistURI, country="US")

i = 0
while(i < 9):
    artistSongs.append(songs['tracks'][i]['uri'])
    i = i + 1

allPlaylists = spotifyObject.user_playlists(user=username)
playlist = allPlaylists["items"][0]["id"]
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=artistSongs) 