# Spotify Playlist to Liked Songs

This Python script allows you to add all tracks from a Spotify playlist to your "Liked Songs" playlist. The script uses the Spotify Web API and the `spotipy` library to authenticate your account and perform the necessary actions.

## Features

- Adds all songs from a specified Spotify playlist to your "Liked Songs".
- Simple command-line interface for ease of use.
- Secure authentication using Spotify's OAuth 2.0.

## Prerequisites

- Python 3.7 or higher
- Spotify Developer account

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/spotify-playlist-to-liked-songs.git
    cd spotify-playlist-to-liked-songs
    ```

2. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Create a Spotify Developer Application**:

   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create a new application.
   - Add `http://localhost:8888/callback` as a Redirect URI.
   - Obtain your `Client ID` and `Client Secret`.

## Usage

1. **Run the script**:

    ```bash
    python main.py
    ```

2. **Follow the prompts**:

   - You will be asked to enter your Spotify `Client ID` and `Client Secret`.
   - After entering the credentials, you will be redirected to a Spotify login page to authorize the application.
   - Once authorized, you can input the link to the playlist you want to add to your liked songs.

3. **Enjoy your music**:
   
   - The script will automatically add all the songs from the playlist to your "Liked Songs" on Spotify.

## Example

Here’s how a session might look:

```bash
$ python main.py
Enter your Spotify Client ID: your-client-id
Enter your Spotify Client Secret: your-client-secret
Enter the playlist link: https://open.spotify.com/playlist/xxxxxx
Adding songs to your liked songs...
Added 50 songs to your liked songs.
 
