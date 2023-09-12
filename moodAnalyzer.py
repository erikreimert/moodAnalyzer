import warnings

from textblob import TextBlob
import librosa
import madmom
import numpy as np


class MoodAnalyzer:
    def __init__(self, sp):
        self.sp = sp

    @staticmethod
    def get_tempo(file_path):
        # Load audio file
        y, sr = librosa.load(file_path)

        # Extract tempo
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

        return tempo

    @staticmethod
    def get_lyrical_sentiment(lyrics):
        blob = TextBlob(lyrics)
        sentiment = blob.sentiment.polarity
        return sentiment

    @staticmethod
    def get_key(file_path):
        # Load the CNN key detection processor
        key_processor = madmom.features.key.CNNKeyRecognitionProcessor()

        # Load the audio file
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            audio, sample_rate = madmom.io.audio.load_audio_file(file_path)

        # Process the audio to get key estimate
        key_estimation = key_processor(audio)

        # Get the estimated key
        key_probabilities = key_estimation[0]

        # Get the index of the maximum value, which corresponds to the estimated key
        estimated_key_index = np.argmax(key_probabilities)

        # Define a list of possible key names
        key_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        # Get the estimated key name
        estimated_key = key_names[estimated_key_index % 12]

        return estimated_key

    @staticmethod
    def get_energy(file_path):
        y, sr = librosa.load(file_path)
        rms_energy = np.sqrt(np.mean(np.square(y)))  # root mean squared
        return rms_energy

    def analyze_music(self, file_path, track_uri, lyrics):
        tempo = self.get_tempo(file_path)
        key = self.get_key(file_path)
        # energy = self.sp.get_energy_level(track_uri)  # offloaded to spotipy for ease of use
        energy = self.get_energy(file_path)  # rms of midi
        # sentiment = self.get_lyrical_sentiment(lyrics)

        return {
            "tempo": tempo,
            "key": key,
            "energy": energy,
            # "sentiment": sentiment
        }
