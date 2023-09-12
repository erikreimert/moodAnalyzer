from API.GeniusInterface import GeniusInterface
from API.SpotipyInterface import SpotipyInterface
from moodAnalyzer import MoodAnalyzer


class MusicProcessor:
    def __init__(self, songs):
        self.sp = SpotipyInterface()
        self.songs = songs
        self.moodAnalyzer = MoodAnalyzer(self.sp)
        self.genius = GeniusInterface()

    def process_songs(self, songs):
        inputData = {}

        # for song in songs:
        file_path = r'C:\Users\erikr\Documents\PyCharm\musicMood\Slow Dancing in a Burning Room [Live].wav'
            # track_name = song['track_name']
            # artist_name = song['artist_name']
            # external API calls
            # track_uri = self.sp.get_track_uri(track_name, artist_name)
            # lyrics = self.genius.get_lyrics(track_name, artist_name)

        result = self.moodAnalyzer.analyze_music(file_path, None, None)

            # inputData[f"{track_name}_{artist_name}"] = result

        return result
