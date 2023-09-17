from API.GeniusInterface import GeniusInterface
from API.SpotipyInterface import SpotipyInterface
from constants import directory
from moodAnalyzer import MoodAnalyzer
import os


class MusicProcessor:
    def __init__(self):
        self.sp = SpotipyInterface()
        self.moodAnalyzer = MoodAnalyzer(self.sp)
        self.genius = GeniusInterface()

    def process_songs(self):
        result = []
        analysis = None

        # for song in songs:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.wav'):
                    file_path = os.path.join(root, file)
                    analysis = self.moodAnalyzer.analyze_music(file_path, None, None)
                    if analysis is not None:
                        result.append(analysis)
            print(f"Finished {root}")

        return result
