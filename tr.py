import os
import time

def list_mp4_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith('.mp4')]

def open_file(filename):
    os.startfile(filename)

directory = "files"

while True:
    files = list_mp4_files(directory)
    os.system('cls')

    if files:
        print("Available media:")
        for idx, file in enumerate(files, start=1):
            print(f"{idx}. {file}")

        try:
            choice = int(input("Enter the media number (or 0 to exit): ")) - 1

            if choice == -1:
                print("Exiting...")
                break

            if 0 <= choice < len(files):
                open_file(os.path.join(directory, files[choice]))
            else:
                print("Wrong number of media. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("No media files found in the directory.")

    time.sleep(1)