from constants import credentials
import requests


class GeniusInterface:
    def __init__(self):
        self.geniusCredentials = credentials['genius']
        self.genius_token = self.geniusCredentials['genius_token']
        self.base_url = 'https://api.genius.com'
        self.search_url = f'{self.base_url}/search'

    def get_lyrics(self, track_name, artist_name):
        # Set up Genius API credentials

        # Prepare headers for API request
        headers = {'Authorization': f'Bearer {self.genius_token}'}

        # Search for the lyrics
        params = {'q': f'{track_name} {artist_name}'}
        response = requests.get(self.search_url, params=params, headers=headers)
        data = response.json()

        # Extract the URL of the lyrics page
        lyrics_url = data['response']['hits'][0]['result']['path']

        # Get the lyrics from the Genius website
        lyrics_response = requests.get(f'{self.base_url}{lyrics_url}')
        lyrics_content = lyrics_response.text

        return lyrics_content
