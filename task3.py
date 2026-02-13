import os
import shutil

# Path of the folder to organize
folder_path = "LEVEL3" 

# File type mapping
file_types = {
    "PDF": [".pdf"],
    "Images": [".jpg", ".png", ".jpeg"],
    "Music": [".mp3", ".wav"],
    "Documents": [".docx", ".txt"]
}

# Loop through all files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                dest_folder = os.path.join(folder_path, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, dest_folder)
                break

print("Folder organized successfully ✅")
