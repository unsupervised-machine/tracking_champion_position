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