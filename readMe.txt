*** Music Mood Analyzer
This Python script provides a mood analysis for a collection of songs based on their tempo, energy, and key. It utilizes various data processing and machine learning techniques.

** Dependencies:

librosa: A package for music and audio analysis.
madmom: A library for audio and music signal processing.
ffmpeg : Download and add to the project folder to be able to convert your mp3s to wav if needed
textblob
csv
numpy
scikit-learn (sklearn)
matplotlib

** Key Files
* moodAnalyzer:
Loads data from a CSV file containing information about tempo, energy, and key of songs.
Extracts features (tempo and energy) from the dataset.
Normalizes the features using standardization.
Encodes the categorical 'key' using one-hot encoding.
Combines the normalized features with the encoded key.
Applies K-means clustering to group songs into mood clusters.

* keyFeatureExtractor:
get_tempo(file_path): This method takes the path to an audio file and extracts its tempo, which represents the beats per minute (BPM) of the music.

get_key(file_path): Given an audio file, this method estimates the musical key it is in (e.g., C major, D minor).

get_energy(file_path): This function calculates the root mean squared (RMS) energy of an audio file. This metric is often used to quantify the overall loudness or intensity of a piece of music.

get_lyrical_sentiment(lyrics): Given a set of lyrics, this method analyzes the sentiment (positive or negative) and returns a polarity score.

analyze_music(file_path, track_uri, lyrics): This method combines the above features to perform a comprehensive analysis of a music file. It calculates the tempo, key, and energy level of the audio. Note that sentiment analysis is commented out in this method.

The code uses the librosa library for audio processing, madmom for key estimation, and TextBlob for sentiment analysis.

** Running the program
To run this install the dependencies and run the main file

Note
The sentiment analysis feature (get_lyrical_sentiment) is currently commented out in the analyze_music method. Uncomment it if you want to use this feature.
Ensure that your data is formatted correctly in the CSV file (inputData.csv).
Adjust the number of clusters (n_clusters) in the moodAnalyzer function as needed for your specific analysis.

