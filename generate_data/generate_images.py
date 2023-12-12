import gzip
import shutil
import zipfile
from pathlib import Path
import yaml
import bpy



def load_mapping_file(file_path):
    """
    Load mapping yaml file for champions and skins.
    :param: string file_path which contains mapping yaml file
    :return: dictionary mapping champion name and skins to their corresponding ids
    """
    with open(file_path, 'r') as yaml_file:
        champion_skin_mapping = yaml.safe_load(yaml_file)
    return champion_skin_mapping


def unzip_model(champion_id
               , skin_id
               , mapping
               , zipped_model_directory='getting_website_data/model_files'
               , model_image_directory='generate_data/images'
               ):
    """
    Unzip and copy model files to the image directory.

    :param champion_id: ID of the champion.
    :param skin_id: ID of the skin.
    :param mapping: Champion-skin mapping.
    :param zipped_model_directory: Directory containing zipped model files.
    :param model_image_directory: Directory for the unzipped model files.
    """
    input_file = Path(zipped_model_directory) / mapping[champion_id]['name'] / mapping[champion_id]['skins'][skin_id]['name'] / f"{mapping[champion_id]['name']}.glb.gz"
    output_file = Path(model_image_directory) / mapping[champion_id]['name'] / mapping[champion_id]['skins'][skin_id]['name'] / f"{mapping[champion_id]['name']}.glb"
    # print(input_file)
    # print(output_file)

    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with gzip.open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    except FileNotFoundError:
        print(f"Input file {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



#  load_model test1: gets correct file names? Yep!
# data_mapping = load_mapping_file('getting_website_data/champion_skin_mapping_small.yaml')
# unzip_model(266000, 0, mapping=data_mapping)
# End of test1
# load_model test2: does it properly unzip file? Yep!
# unzip_model(266000, 0, mapping=data_mapping)
# End of test2

def create_model_images(output_folder):
    """
    Expects blender to be open with appropriate set up for generating images for this project...
    Looks for model file inside of output_folder if found:
        Delete previous objects in scene.
        Import current model.
        Create images for current model, save them in output folder.
    :param output_folder:
    :return:
    """
    pass


def delete_unzipped_models(output_folder):
    """
    deletes unzipped models inside output_folder
    :param output_folder:
    :return:
    """
    pass





