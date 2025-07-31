import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        source = os.path.join(folder_path, filename)
        if os.path.isfile(source):
            ext = filename.split('.')[-1]
            dest_folder = os.path.join(folder_path, ext + "_files")
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(source, os.path.join(dest_folder, filename))

folder = input("Enter folder path to organize: ")
organize_files(folder)
print("Files organized successfully.")
