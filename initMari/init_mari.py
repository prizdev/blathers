import mari, os

taskname = os.listdir('C:\\prizmiq')
taskname = str(taskname[0])

EmptyChannels = []
project_meta_options = dict()
project_meta_options["MultipleGeometries"] = mari.projects.MERGE_GEOMETRIES
project_meta_options["MergeType"] = mari.geo.MERGETYPE_SINGLE_MESH
project_meta_options["CreateSelectionSets"] = mari.geo.SELECTION_GROUPS_CREATE_FROM_FACE_GROUPS
obj_file = 'C:\\prizmiq\\123456\\texture\\serverDown\\geometry.obj'
try:
    mari.projects.create(taskname, obj_file, EmptyChannels, EmptyChannels, project_meta_options)
except:
    pass
