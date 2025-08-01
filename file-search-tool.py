import os

def search_files(directory, keyword):
    for root, _, files in os.walk(directory):
        for file in files:
            if keyword.lower() in file.lower():
                print(os.path.join(root, file))

folder = input("Enter folder path: ")
word = input("Enter keyword to search: ")
search_files(folder, word)
