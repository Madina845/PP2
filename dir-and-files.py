import os
import shutil
import time
import math

# 1. List only directories, files, and all directories in a specified path
def list_directories_files(path):
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All items:", os.listdir(path))

# 2. Check for access to a specified path
def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

# 3. Check if a path exists, and extract filename and directory
def path_info(path):
    if os.path.exists(path):
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist")

# 4. Count the number of lines in a text file
def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for _ in file)

# 5. Write a list to a file
def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.writelines('\n'.join(data))

# 6. Generate 26 text files (A.txt to Z.txt)
def generate_text_files():
    for letter in range(65, 91):  # ASCII codes for A-Z
        with open(f"{chr(letter)}.txt", "w") as file:
            file.write(f"File {chr(letter)}")

# 7. Copy contents of a file to another file
def copy_file(source, destination):
    shutil.copyfile(source, destination)

# 8. Delete file, checking access and existence
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted")
    else:
        print("File does not exist or not writable")