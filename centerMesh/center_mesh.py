import bpy

bl_info = {
'name': 'Centering Mesh',
'category': 'Object'
}

class CenterMesh(bpy.types.Operator):
    bl_idname  = 'object.center_mesh'
    bl_label   = 'Center Mesh'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        ###################  PART ONE  ####################

        try:

            if bpy.data.objects['Empty'] in list(bpy.data.objects):

                bpy.ops.view3d.viewnumpad(type = 'CAMERA')

                for obj in bpy.data.objects:
                    obj.select = False
                bpy.ops.object.select_pattern(pattern = 'geo*')

                selList = []
                for obj in bpy.data.objects:
                    if obj.select == True:
                        selList.append(obj)
                obj = selList[0]

                bpy.context.scene.objects.active = bpy.data.objects['Camera']
                bpy.data.objects['Camera'].select = True
                bpy.ops.object.parent_set()
                bpy.data.objects['Camera'].select = False
                bpy.data.objects['Camera'].rotation_euler = [1.5708, 0, 0]
                bpy.ops.object.parent_clear(type = 'CLEAR_KEEP_TRANSFORM')
                obj.location = [0, 0, 0]

                bbVerts = list(obj.bound_box)
                bbMax   = 0
                for vert in bbVerts:
                    for coord in vert:
                        if abs(coord) > bbMax:
                            bbMax = abs(coord)

                obj.scale    = [8 / bbMax, 8 / bbMax, 8 / bbMax]
                bpy.ops.object.transform_apply(location = True, rotation = True, scale = True)

                bpy.context.scene.objects.active = obj
                bpy.ops.export_scene.obj(filepath = 'C:\\prizmiq\\123456\\model\\serverUp\\geoCentered.obj', check_existing = False, use_selection = True, use_materials = False)

                return {'FINISHED'}


        ###################  PART TWO  ####################

        except KeyError:

            bpy.ops.scene.gob_import()

            for obj in bpy.data.objects:
                obj.select = False
            bpy.ops.object.select_pattern(pattern = 'geo*')

            selList = []
            for obj in bpy.data.objects:
                if obj.select == True:
                    selList.append(obj)
            obj = selList[0]

            bpy.context.scene.objects.active = obj
            bpy.ops.object.origin_set(type = 'GEOMETRY_ORIGIN', center = 'BOUNDS')
            bpy.ops.view3d.viewnumpad(type = 'CAMERA')
            bpy.context.space_data.lock_camera = True
            bpy.ops.object.empty_add()
            bpy.ops.export_scene.obj(filepath = 'C:\\prizmiq\\123456\\model\\serverUp\\geoTexture.obj', check_existing = False, use_materials = False)

            return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(CenterMesh.bl_idname)

addon_keymaps = []

def register():
    bpy.utils.register_class(CenterMesh)
    bpy.types.VIEW3D_MT_object.append(menu_func)

    wm  = bpy.context.window_manager
    km  = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(CenterMesh.bl_idname, 'SPACE', 'PRESS', ctrl = True, shift = True)
    #kmi.properties.total = 4
    addon_keymaps.append(km)


def unregister():
    bpy.utils.unregister_class(CenterMesh)

    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    del addon_keymaps[:]

if __name__ == '__main__':
    register()
