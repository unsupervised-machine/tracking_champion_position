import gzip
import shutil
import zipfile
from pathlib import Path
import yaml


with open('getting_website_data/champion_skin_mapping_small.yaml', 'r') as yaml_file:
    champion_skin_mapping = yaml.safe_load(yaml_file)

zipped_model_directory = 'getting_website_data/model_files'
model_image_directory = 'generate_data/images'

for champion in champion_skin_mapping:
    zipped_file = Path(zipped_model_directory) / f"{champion['name']}"
    print(zipped_file)



