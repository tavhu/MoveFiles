import os
import shutil

def move_files_to_new_folders():
    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    file_count = len(files)

    if file_count <= 200:
        # If there are 200 or fewer files, move them to a new folder with the same name as the current directory
        new_folder = os.path.join(current_dir, os.path.basename(current_dir))
        os.makedirs(new_folder, exist_ok=True)
        for file in files:
            if file == "moveFiles.exe":  # Skip moving the executable file
                continue
            file_path = os.path.join(current_dir, file)
            if os.path.isfile(file_path):
                shutil.move(file_path, new_folder)
    else:
        # If there are more than 200 files, create numbered folders and move files accordingly
        num_folders = file_count // 200 + (file_count % 200 > 0)  # Calculate the number of folders needed
        for i in range(num_folders):
            folder_name = f"{os.path.basename(current_dir)}_{i+1}"
            new_folder = os.path.join(current_dir, folder_name)
            os.makedirs(new_folder, exist_ok=True)
            for j in range(200):
                file_index = i * 200 + j
                if file_index >= file_count:
                    break
                file = files[file_index]
                if file == "moveFiles.exe":  # Skip moving the executable file
                    continue
                file_path = os.path.join(current_dir, file)
                if os.path.isfile(file_path):
                    shutil.move(file_path, new_folder)

if __name__ == "__main__":
    move_files_to_new_folders()