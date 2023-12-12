# looks like I will refactor this script into blender_script.py manipulate_file function to unzip model,
# take and save pictures then eventually delete unzipped model once we are done with it

import gzip
import shutil
import zipfile
from pathlib import Path
import yaml




zipped_model_directory = 'getting_website_data/model_files'
model_image_directory = 'generate_data/images'

with open('getting_website_data/champion_skin_mapping_small.yaml', 'r') as yaml_file:
    champion_skin_mapping = yaml.safe_load(yaml_file)

for champion in champion_skin_mapping:
    for skin in champion['skins']:
        zipped_file = Path(zipped_model_directory) / f"{champion['name']}" / f"{skin['name']}" / f"{champion['name']}.glb.gz"
        output_file = Path(model_image_directory) / f"{champion['name']}" / f"{skin['name']}" / f"{skin['name']}.glb"

        # print(zipped_file)
        # print(output_file)
        # output_file.touch()
        if not zipped_file.is_file():
            print(f"input file {zipped_file} does not exist")
            continue

        with gzip.open(zipped_file, 'rb') as f_in:
            print(f_in)

            with open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)





