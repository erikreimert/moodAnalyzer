from musicProcessor import MusicProcessor
from wavGen import process_directory
import csv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    musicProcessor = MusicProcessor()
    inputData = musicProcessor.process_songs()

    # store input into csv file
    with open('inputData.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['tempo', 'key', 'energy'])
        writer.writeheader()
        for row in inputData:
            writer.writerow(row)

    print(inputData)

    # root_directory = r"D:\fma_large"
    # Call the function to start the conversion process
    # process_directory(root_directory)
