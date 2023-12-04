import bpy
import os



def deleteAllObjects():
    """
    Deletes all objects in the current scene
    :return:
    """
    deleteListObjects = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'HAIR', 'POINTCLOUD', 'VOLUME', 'GPENCIL',
                         'ARMATURE', 'LATTICE', 'EMPTY', 'LIGHT', 'LIGHT_PROBE', 'CAMERA', 'SPEAKER']

    # Select all objects in the scene to be deleted:

    for o in bpy.context.scene.objects:
        for i in deleteListObjects:
            if o.type == i:
                o.select_set(False)
            else:
                o.select_set(True)
    bpy.ops.object.delete()  # Deletes all selected objects in the scene

# deleteAllObjects()
# bpy.ops.import_scene.gltf("/home/taran/Documents/test_projects/tracking_champion_position/generate_data/sample_data/ahri_files/ahri.glb")
filepath = "generate_data/sample_data/aatrox_files/aatrox.glb"
bpy.ops.import_scene.gltf(filepath=filepath)

# print all objects
for ob in bpy.data.objects:
    print(ob.name)
    try:
        ob.material_slot_remove()
        print("removed material from " + ob.name)
    except:
        print(ob.name + " does not have materials.")

list(bpy.data.objects)

for obj in list(bpy.data.objects):
    obj.select_set(False)

subject = bpy.data.objects["mesh_0"]
subject.select_set(True)

bpy.ops.view3d.camera_to_view_selected()


bpy.context.scene.render.filepath = "generate_data/sample_data/aatrox_files/jpeg_folder/image_1"
bpy.context.scene.render.image_settings.file_format = "JPEG"# Set image file format
bpy.ops.render.render(write_still=True)




### GPT SCTIPT
import bpy

filepath = "generate_data/sample_data/aatrox_files/aatrox.glb"
bpy.ops.import_scene.gltf(filepath=filepath)

# Set the scene resolution
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080

# Set the output format to JPEG
bpy.context.scene.render.image_settings.file_format = 'JPEG'

# Set the output path
bpy.context.scene.render.filepath = "generate_data/sample_data/aatrox_files/jpeg_folder/image_1"

# Create a new camera
bpy.ops.object.camera_add(location=(0, -5, 5))  # Set the initial location of the camera
new_camera = bpy.context.active_object
new_camera.name = "MyCamera"

# Set the active object to the desired mesh (assuming its name is "mesh_0")
mesh_object = bpy.data.objects.get("mesh_0")

if mesh_object and new_camera:
    # Set the camera to focus on the mesh
    bpy.ops.object.select_all(action='DESELECT')
    mesh_object.select_set(True)
    bpy.context.view_layer.objects.active = mesh_object

    # Set the camera to look at the selected object
    bpy.ops.view3d.camera_to_view_selected()

    # Optionally adjust camera settings (e.g., focal length)
    new_camera.data.lens = 50  # Adjust the focal length as needed

    # Set the camera as the active object
    bpy.context.view_layer.objects.active = new_camera

# Render the image
bpy.ops.render.render(write_still=True)


# Set up rendering settings
bpy.context.scene.render.image_settings.file_format = 'JPEG'
bpy.context.scene.render.filepath = "/home/taran/Documents/test_projects/tracking_champion_position/generate_data/sample_data/aatrox_files/jpeg_folder/image_1.jpg"  # Output path (in the same directory as the .blend file)


bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
# Render the scene
bpy.ops.render.render(write_still=True)

import bpy

# Initial
old_objects = ["Cube"]

# start loop
# Import
bpy.ops.import_scene.gltf(filepath="/home/taran/Documents/test_projects/tracking_champion_position/generate_data/sample_data/ahri_files/ahri.glb")

# Imported objects are selected
new_objects = [o.name for o in bpy.context.selected_objects]

# Drop old objects
for o in old_objects:
    bpy.data.objects.remove(bpy.data.objects[o], do_unlink=True)

# Render Image
# do this later
bpy.data.objects["da421925-ca68-43db-973c-bd07a5570295"].hide_viewport = True

# bpy.types.RenderSettings.views_format('MULTIVIEW')
# bpy.types.RenderSettings.use_multiview()
# Not quite working but close
# It works now woohoo!!!
import bpy
bpy.context.scene.render.filepath = '/home/taran/Documents/test_projects/tracking_champion_position/generate_data/sample_data/ahri_files/pls_empty/ahri.jpg'
bpy.types.RenderSettings.views_format = 'MULTIVIEW'
bpy.context.scene.render.image_settings.file_format = "JPEG"
bpy.ops.render.render(write_still=True)


# Set New objs to old
old_objects = new_objects

# end of loop ( import more new objects )


# for object in bpy.context.scene.objects:
#    print(object.name)


import bpy

#for object in bpy.context.scene.objects:
#    print(object.name)

old_objects = ["341b811b-e1d7-4d30-855b-2facd3addbe9"]

# Import
bpy.ops.import_scene.gltf(filepath="/home/taran/Documents/test_projects/tracking_champion_position/generate_data/sample_data/ahri_files/ahri.glb")

# Imported objects are selected
new_objects = [o.name for o in bpy.context.selected_objects]


# Drop old objects
for o in old_objects:
    bpy.data.objects.remove(bpy.data.objects[o], do_unlink=True)

# Render Image

bpy.data.objects["da421925-ca68-43db-973c-bd07a5570295"].hide_viewport = True
bpy.context.scene.render.filepath = '/home/taran/Documents/test_projects/tracking_champion_position/generate_data/sample_data/ahri_files/pls_empty/ahri.jpg'
bpy.types.RenderSettings.views_format = 'MULTIVIEW'
bpy.context.scene.render.image_settings.file_format = "JPEG"
bpy.ops.render.render(write_still=True)


# Set New objs to old
old_objects = new_objects





import bpy

for object in bpy.context.scene.objects:
    print(object.name)
    print(object.type)

old_objects = ["58be6483-0e4e-49ca-8a8a-d67142f4f96d"]
#old_objects = ["341b811b-e1d7-4d30-855b-2facd3addbe9.001"]


# Import
bpy.ops.import_scene.gltf(filepath="/home/taran/Documents/test_projects/tracking_champion_position/generate_data/sample_data/ahri_files/ahri.glb")


# Drop old objects ... try doing this before import?
for o in old_objects:
    bpy.data.objects.remove(bpy.data.objects[o], do_unlink=True)

# Imported objects are selected
new_objects = [o.name for o in bpy.context.selected_objects]


# Drop old objects ... try doing this before import?
for o in old_objects:
    bpy.data.objects.remove(bpy.data.objects[o], do_unlink=True)

# Render Image
for object in bpy.context.scene.objects:
    if object.type == "ARMATURE":
        # hide_this
        bpy.data.objects[object.name].hide_viewport = True

#bpy.data.objects["da421925-ca68-43db-973c-bd07a5570295"].hide_viewport = True
bpy.context.scene.render.filepath = '/home/taran/Documents/test_projects/tracking_champion_position/generate_data/sample_data/ahri_files/pls_empty/ahri.jpg'
bpy.types.RenderSettings.views_format = 'MULTIVIEW'
bpy.context.scene.render.image_settings.file_format = "JPEG"
bpy.ops.render.render(write_still=True)


# Set New objs to old
old_objects = new_objects








# Done ?
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


