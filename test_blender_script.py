import bpy

deleteListObjects = [
    # 'MESH',
    # 'CURVE',
    # 'SURFACE',
    # 'META',
    # 'FONT',
    # 'HAIR',
    # 'POINTCLOUD',
    # 'VOLUME',
    # 'GPENCIL',
    # 'ARMATURE',
    # 'LATTICE',
    # 'EMPTY',
    # 'LIGHT',
    # 'LIGHT_PROBE',
    # 'SPEAKER',
    'CAMERA'
    ]

for o in bpy.context.scene.objects:
    for i in deleteListObjects:
        if o.type == i:
            o.select_set(False)
        else:
            o.select_set(True)

# delete existing objects
bpy.ops.object.delete()

bpy.ops.import_scene.gltf(
    filepath="/home/taran/Documents/test_projects/tracking_champion_position/generate_data/sample_data/ahri_files/ahri.glb")

for object in bpy.context.scene.objects:
    if object.type == "ARMATURE":
        # hide_this
        bpy.data.objects[object.name].hide_viewport = True

bpy.context.scene.render.filepath = '/home/taran/Documents/test_projects/tracking_champion_position/generate_data/sample_data/ahri_files/pls_empty/ahri.jpg'
bpy.types.RenderSettings.views_format = 'MULTIVIEW'
bpy.context.scene.render.image_settings.file_format = "JPEG"
bpy.ops.render.render(write_still=True)

# Run these in terminal to run this script in blender
# blender /home/taran/Documents/test_projects/tracking_champion_position/generate_data/sample_data/cameras/cameras_positioned_v3.blend
# blender /home/taran/Documents/test_projects/tracking_champion_position/generate_data/sample_data/cameras/cameras_positioned_v3.blend --python /home/taran/Documents/test_projects/tracking_champion_position/test_blender_script.py