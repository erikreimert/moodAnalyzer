import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from constants import credentials


class SpotipyInterface:
    def __init__(self):
        # Set up Spotify API credentials
        self.spotifyCredentials = credentials['spotipy']
        self.client_id = self.spotifyCredentials['client_id']
        self.client_secret = self.spotifyCredentials['client_secret']

        # Initialize Spotify API client
        client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id,
                                                              client_secret=self.client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_energy_level(self, track_uri):
        # Get track features from Spotify API
        track_features = self.sp.audio_features(track_uri)

        # Extract energy level
        energy = track_features[0]['energy']
        return energy

    def get_track_uri(self, track_name, artist_name):
        # Search for a track
        results = self.sp.search(q=f'track:{track_name}:{artist_name}', type='track', limit=1)

        # Get the track URI
        return results['tracks']['items'][0]['uri']
