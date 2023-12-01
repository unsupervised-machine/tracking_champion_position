import os
import zipfile
import shutil
from pathlib import Path

import  requests
from ultralytics import YOLO
model = YOLO('yolov8n.pt')

with zipfile.ZipFile('datasets/valorant_datasets/valorant-object-detection2.v4i.yolov8.zip', 'r') as zip_ref:
    print('Unzipping valorant data...')
    zip_ref.extractall('datasets/valorant_datasets/valorant')

yaml_path = 'datasets/valorant_datasets/valorant/data.yaml'
yaml_path = 'datasets/valorant_datasets/valorant/data.yaml'


results = model.train(data=yaml_path)

# need to edit yaml file before training. it is looking in the wrong directories for the images.
