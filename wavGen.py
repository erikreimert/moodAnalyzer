import os
import subprocess


# Define the function for converting files
def convert_to_wav(input_file):
    ffmpeg_path = r'ffmpeg-master-latest-win64-gpl/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe'  # Replace with your actual path
    output_file = os.path.splitext(input_file)[0] + '.wav'
    subprocess.run([ffmpeg_path, '-i', input_file, output_file])
    os.remove(input_file)  # Add this line to delete the original .mp3 file


# Define the function for processing directories recursively
def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.mp3')):
                input_file = os.path.join(root, file)
                convert_to_wav(input_file)