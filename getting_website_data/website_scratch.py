import sys
import re
import requests
import yaml
from pathlib import Path
def get_cloudfront_url():
    # Get Cloud Front Url
    # Used to get champion models like this:
    # https://d39h8efa1lafbi.cloudfront.net/export/22/skin65.glb.gz
    # where 22 is the champion ID and 65 is the skin ID (not the offset)
    api_url = "https://www.modelviewer.lol/en-US/model-viewer"
    response = requests.get(api_url)
    response_text = response.text
    pattern = re.compile(r'<script src="/_next/static/chunks/pages/(_app.*?\.js)" defer>')
    match = re.search(pattern, response_text)
    matched_string = match.group(1)
    print(matched_string)

    api_url = f"https://www.modelviewer.lol/_next/static/chunks/pages/{matched_string}"
    response = requests.get(api_url)
    response_text = response.text
    pattern = re.compile(r'https://([^/]+)\.cloudfront\.net/export')
    match = re.search(pattern, response_text)
    matched_string = match.group()
    # This is the cloudfront url
    # print(matched_string)
    # https://d39h8efa1lafbi.cloudfront.net/export
    return matched_string


# Get champion IDs
def create_champions_data():
    api_url = "https://www.modelviewer.lol/api/champions?language=default"
    response = requests.get(api_url)
    champions_data = 'Failed to get champion IDs'
    if response.status_code == 200:
        # Print the response content (usually in JSON format for APIs)
        print("Response:")
        print(response.json())
        champion_data = response.json()  # this is a alphabetically sorted list of champion ids dictionaries
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
    return champions_data


# TODO create rate limit back off functionality
def add_skin_data(champions_data):
    for d in champion_ids:
        champions_name = d['name']
        champion_id = d['id']
        api_url = f"https://www.modelviewer.lol/api/skins?id={champion_id}&language=default"
        response = requests.get(api_url)
        champion_skin_ids = response.json()
        d['skins_data'] = champion_skin_ids
    return None # we are modifying champions_data

def save_champion_skin_mapping(champions_data, file_path='getting_website_data/champion_skin_mapping.yaml'):
    with open(file_path, 'w') as yaml_file:
        yaml.dump(champions_data, yaml_file)
    return None  # we saved the file

# save_champion_skin_data(champion_ids)
# with open('getting_website_data/champions_data.yaml', 'r') as yaml_file:
#     loaded_data = yaml.safe_load(yaml_file)
def load_yaml_file(file_path):
    with open(file_path, 'r') as yaml_file:
        loaded_data = yaml.safe_load(yaml_file)
    return loaded_data



# The text that you found from Step 4 is the full cloudfront url!
# Now create the URLs to specific blender models like we did above.
# For example, https://d39h8efa1lafbi.cloudfront.net/export/22/skin65.glb.gz
# where 22 is the champion ID and 65 is the skin ID (not the offset)

#
# https://d39h8efa1lafbi.cloudfront.net/export/1/skin0.glb.gz Base Annie Skin...
# https://d39h8efa1lafbi.cloudfront.net/export/2/skin0.glb.gz Base Olaf Skin
# https://d39h8efa1lafbi.cloudfront.net/export/92/skin0.glb.gz Base Riven Skin
# https://d39h8efa1lafbi.cloudfront.net/export/38/skin0.glb.gz
# https://d39h8efa1lafbi.cloudfront.net/export/10/skin0.glb.gz
# champion_id = id + 000
# riven_id = 92000 = 92 + 000  -> base riven skin
# ashe_id = 22000 = 22 + 000 -> base ashe skin
# ashe_id = 22065 = 22 + 065 -> crystal ashe

# https://d39h8efa1lafbi.cloudfront.net/export
def get_download_url(cloudfront_url
                   , champion_skin_id=103000
                   ):
    champion_id = str(champion_skin_id)[:-3]
    # print(champion_id)
    # print(type(champion_id))
    skin_id = str(champion_skin_id)[-3:].lstrip('0')
    if not skin_id:
        skin_id = '0'
    # api_url = f"https://{cloudfront_url}.cloudfront.net/export/{champion_id}/skin{skin_id}.glb.gz"
    api_url = f"{cloudfront_url}/{champion_id}/skin{skin_id}.glb.gz"

    return api_url

# get_download_url(cloudfront_url)



def get_many_models(cloudfront_url
                    , run_type='all_base'  # all_skins/all_base/select
                    , selection_list=None  # used when run_type='select', list of tuples (champion, skin)
                    , replace_existing=False  # 'True/False'
                    , mapping_file='getting_website_data/champion_skin_mapping.yaml'
                    , save_files_directory=Path('getting_website_data/model_files')
                    ):
    responses = []
    champion_skin_data = load_yaml_file(mapping_file)

    # if not save_files_directory.exists():
    #     print('Please specify which directory to save champion folders...')
    #     sys.exit()

    if run_type == 'all_skins':
        pass

    if run_type == 'select':
        models_to_collect = selection_list
        pass

    if run_type == 'all_base':
        for d in champion_skin_data:
            champion_name = d['name']
            champion_id = d['id']
            skin_name = champion_name
            output_folder = save_files_directory / champion_name / skin_name
            output_folder.mkdir(parents=True, exist_ok=True)
            # print(output_folder)
            # print(champion_id)
            # print(skin_name)
            # print(cloudfront_url)
            print(champion_id)
            print(type(champion_id))
            api_url = get_download_url(cloudfront_url
                                       , champion_skin_id=champion_id
                                       )
            filename = output_folder / (skin_name + ".glb.gz")
            # filename = output_folder / (skin_name + ".glb")
            if not replace_existing and filename.exists():
                print(f"file already exists and replace_existing set to False, skipping {filename}")
                continue

            print(f"Download url {api_url} into {filename}")
            response = requests.get(api_url)
            # response.encoding = 'gzip'
            # responses.append(response)
            response = requests.get(api_url, stream=True)

            with open(filename, 'wb') as file:
                for chunk in response.raw.stream(1024, decode_content=False):
                    if chunk:
                        file.write(chunk)
                # file.write(response.content)
            print(f"Downloaded into {filename}")
    return responses


# Testing 09122023
cloudfront_url = get_cloudfront_url()
small_champ_ids = champion_ids[0:5]
# save_champion_skin_mapping(small_champ_ids, file_path='getting_website_data/champion_skin_mapping_small.yaml')
# get_many_models(cloudfront_url
#                 , run_type='all_base'  # all_skins/all_base/select
#                 , selection_list=None  # used when run_type='select', list of tuples (champion, skin)
#                 , replace_existing=True  # 'True/False'
#                 , mapping_file='getting_website_data/champion_skin_mapping_small.yaml'
#                 , save_files_directory=Path('getting_website_data/model_files')
#                 )
responses = get_many_models(cloudfront_url
                , run_type='all_base'  # all_skins/all_base/select
                , selection_list=None  # used when run_type='select', list of tuples (champion, skin)
                , replace_existing=True  # 'True/False'
                , mapping_file='getting_website_data/champion_skin_mapping_small.yaml'
                , save_files_directory=Path('getting_website_data/model_files')
                )






# Testing 05122023
# Get Champions
api_url = "https://www.modelviewer.lol/api/champions?language=default"

response = requests.get(api_url)

if response.status_code == 200:
    # Print the response content (usually in JSON format for APIs)
    print("Response:")
    print(response.json())
    champion_ids = response.json() # this is a alphabetically sorted list of champion ids dictionaries
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")
    print("Problem accessing champion IDs data")
    sys.exit()








# Get base model for champion
api_url = "https://www.modelviewer.lol/api/skins?id=103000&language=default"
response = requests.get(api_url)
champion_skin_ids = response.json()
print(champion_skin_ids[0]['id'])




for d in champion_ids:
    # api_url = "https://www.modelviewer.lol/api/skins?id=103000&language=default"
    champion_name = d['name']
    champion_id = d['id']
    api_url = f"https://www.modelviewer.lol/api/skins?id={champion_id}&language=default"
    # print(api_url)
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Response:")
        print(response.json())
        champion_skin_ids = response.json()



test = champion_ids[1]
test['skins_data'] = champion_skin_ids