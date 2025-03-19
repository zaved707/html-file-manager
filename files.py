from pathlib import Path
import shutil
import os
import json

def up_dir(dir_string,devider): 
    # Find the last occurrence of '/' using rindex()
    last_slash_index = dir_string.rindex(devider)
    # Return the substring from the start up to (but not including) the last slash
    return dir_string[:last_slash_index]

def list_files(directory_path):
    """
    Lists all files in the specified source_dir.

    Args:
        directory_path (str): The path to the source_dir.

    Returns:
        list: A list of file names in the source_dir.
    """
    source_dir = Path(directory_path)
    files=[]
    count=0
    for f in source_dir.iterdir():
        if count>100:
            break
        if f.is_file():
            files.append(f.name)
            count+=1
    return files

def list_folders(directory_path):
    folders = []
    source_dir = Path(directory_path)
    for f in source_dir.iterdir():
        if f.is_dir():  # Changed from is_file() to is_dir()
            folders.append(f.name)
        
    
    return folders

# Function to move files to their respective folders
def organize_files(json_data, source_dir, destination_dir):
    # Create destination folders if they don't exist
    for item in json_data:
        folder_path = os.path.join(destination_dir, item["destination_folder"])
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        source_file = os.path.join(source_dir, item["file_name"])
        destination_file = os.path.join(destination_dir, item["destination_folder"], item["file_name"])

        if os.path.exists(source_file):
            shutil.move(source_file, destination_file)
            print(f"Moved: {item['file_name']} -> {item['destination_folder']}")
        else:
            print(f"File not found: {item['file_name']}")
def organize_revert(json_file_path, source_dir, destination_dir):
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
    for item in json_data:
        file=os.path.join(destination_dir, item["destination_folder"], item["file_name"])
        revert_dir=os.path.join(source_dir, item["file_name"])
        if os.path.exists(file):
            if os.path.exists(revert_dir):
                print('file'+file+'already exists, therefore skipping')
            else:
                shutil.move(file, revert_dir)
        else:
            print('file does not exists...skipping')
    delete_empty_folders(destination_dir)
def delete_empty_folders(source_dir):
    # Traverse the source_dir tree
    for root, dirs, files in os.walk(source_dir, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                # Check if the source_dir is empty
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)  # Delete the empty source_dir
                    print(f"Deleted empty source_dir: {dir_path}")
            except Exception as e:
                print(f"Error deleting {dir_path}: {e}")

# Main program
if __name__ == "__main__":
    # Load JSON data (from a file or string)
    

    # User-defined paths
    source_directory = os.getcwd()+"\\testing folder"
    destination_directory = os.getcwd()+"\\testing folder"
    # Organize files
    json_file_path=os.path.join(os.getcwd(),"last_output.json")
    if os.path.exists(json_file_path):
        pass