import bpy
import os

filepath = "generate_data/sample_data/aatrox_files/aatrox.glb"
bpy.ops.import_scene.gltf(filepath=filepath)

bpy.context.scene.render.filepath = "generate_data/sample_data/aatrox_files/jpeg_folder"
bpy.context.scene.render.image_settings.file_format = "JPEG" # Set image file format
bpy.ops.render.render(write_still=True)