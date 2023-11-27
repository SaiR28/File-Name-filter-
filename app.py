import os
import shutil

def organize_folders(root_folder):
    new_folder_name = os.path.join(root_folder, 'Folders_Containing_Name')
    if not os.path.exists(new_folder_name):
        os.makedirs(new_folder_name)

    folders_to_move = []

    # Identify folders to move
    for foldername, subfolders, filenames in os.walk(root_folder):
        if 'papers' in foldername.lower() or 'paper' in foldername.lower():
            folders_to_move.append(foldername)

    # Move the identified folders (including 'papers' or 'paper' folders)
    for folder_to_move in folders_to_move:
        try:
            destination_folder = new_folder_name if 'papers' in folder_to_move.lower() or 'paper' in folder_to_move.lower() else os.path.join(new_folder_name, os.path.basename(folder_to_move))
            shutil.move(folder_to_move, destination_folder)
        except shutil.Error as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    root_directory = "SEM 5-20231127T164441Z-001"  # Replace with the path to your root directory
    organize_folders(root_directory)
