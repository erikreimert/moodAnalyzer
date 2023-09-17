- music21 didnt work bc MIDI was a pain in the ass
- genius API not implemented because most of hte songs are random AF and thus cant pull from genius
- most songs also not in spotify so I had to do RMS to get my own "energy"
- using a pretrained CNN to get the key of the song
- ideally in the future i could use this with Spotify but they dont let you download music files with their API
- had to transform the mp3 files to wav files
- the database I had already had tons of metadata on the songs but I wanted to do the extracting myself for funsies and practice
- downloaded the music to train the model from https://github.com/mdeff/fma


Note: download ffmpeg and add it to the project folder to be able to convert your mp3s to wav