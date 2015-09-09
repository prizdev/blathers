import bpy
import sys

def main():
    inputObj = str(sys.argv[sys.argv.index('-i') + 1])

    for obj in bpy.data.objects:
        obj.select = True
    bpy.ops.object.delete()

    bpy.ops.object.camera_add()
    bpy.data.objects['Camera'].location       = (10, 10, 10)
    bpy.data.objects['Camera'].rotation_euler = (0.7854, 0, 2.3562)

    bpy.ops.import_scene.obj(filepath = inputObj)

    bpy.ops.scene.gob_export()
    bpy.ops.scene.gob_import()

    bpy.data.objects['geometry'].select = True
    bpy.context.scene.objects.active = bpy.data.objects['geometry']
    bpy.ops.object.delete()


if __name__ == '__main__':
    main()
