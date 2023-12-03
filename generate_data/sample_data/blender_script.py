import os
import sys
from pathlib import Path
import bpy

# blender_script.py
# This will take in a list of champion names and generate a folder of rendered images.
# Example usage python blender_script.py name_list.txt


# run this in blender after opening a cameras file
def manipulate_file(file_path, output_folder):
    # Image manipulation logic goes here
    # This is just a placeholder; replace it with your actual code
    # This part uses blender py


def process_names_from_file(file_path):
    with open(file_path, 'r') as file:
        names = file.read().splitlines()

    for name in names:
        # name = 'ahri'
        # Assuming each name corresponds to a folder
        folder_path = Path(f"~/Documents/test_projects/tracking_champion_position/generate_data/sample_data/{name}" )
        # Assuming each folder has a file with the same name (.glb)
        file_path = folder_path / f"{name}.glb"

        # Check if folder and file exist
        if folder_path.exists() and file_path.is_file():
            # Create a new folder to save the rendered images
            output_folder = folder_path / f"{name}_images"

            output_folder.mkdir(exist_ok=True)

            # Render and save the images (jpg)
            manipulate_file(file_path, output_folder)
            print(f"Images for {name} processed in blender and saved in {output_folder}")
        else:
            print(f"Error: Folder or .glb file not found for {name}")

if __name__ == "__main__":
    if len(sys.argv) !=2: # call this through command line with two arguements
        print("Usage: Python script.py <name_list_file.txt>")
        sys.exit(1)

    name_list_file = Path(sys.argv[1])

    if not name_list_file.exists():
        print(f"Could not find input file {name_list_file}.")
        sys.exit(1)

    # Process the name from the file
    process_names_from_file(name_list_file)
