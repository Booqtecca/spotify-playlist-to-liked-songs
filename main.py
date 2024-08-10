import spotipy
from spotipy.oauth2 import SpotifyOAuth

def main():
    client_id = input("Client ID de Spotify: ")
    client_secret = input("Client Secret de Spotify: ")
    redirect_uri = "http://localhost:8888/callback"
    scope = "playlist-read-private user-library-modify"
    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope
    ))
    
    playlist_link = input("Playlist Link : ")
    add_playlist_to_liked_songs(sp, playlist_link)

def add_playlist_to_liked_songs(sp, playlist_link):
    playlist_id = playlist_link.split("/")[-1].split("?")[0]
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    track_ids = [track['track']['id'] for track in tracks]
    
    for i in range(0, len(track_ids), 50):
        sp.current_user_saved_tracks_add(track_ids[i:i+50])

    print(f"Agregadas {len(track_ids)} canciones a la lista de canciones me gusta.")

if __name__ == "__main__":
    main()
