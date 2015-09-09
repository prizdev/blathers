import mari, os

def main():
    if bool(sys.argv[sys.argv.index('-ib') + 1]) == True:
        initMari()
        connect(mari.projects.aboutToCloseProject, saveChannel)
    else:
        pass


def initVar(switch):
    if switch == 0:
        taskname = os.listdir('C:\\prizmiq')
        taskname = str(taskname[0])
        return taskname
    elif switch == 1:
        geo  = mari.geo.current()
        chan = geo.channel('diffuse')
        return chan
    else:
        pass


def initMari():
    taskname = initVar(0)
    EmptyChannels = []
    project_meta_options = dict()
    project_meta_options["MultipleGeometries"] = mari.projects.MERGE_GEOMETRIES
    project_meta_options["MergeType"] = mari.geo.MERGETYPE_SINGLE_MESH
    project_meta_options["CreateSelectionSets"] = mari.geo.SELECTION_GROUPS_CREATE_FROM_FACE_GROUPS
    obj_file = 'C:\\prizmiq\\%s\\texture\\serverDown\\geometry.obj' % taskname
    try:
        mari.projects.create(taskname, obj_file, EmptyChannels, EmptyChannels, project_meta_options)
    except:
        pass

    chan = initVar(1)

    chan.importImages('C:\\prizmiq\\%s\\texture\\serverDown\\diffuse.$UDIM.jpg' % taskname)


def saveChannel():
    taskname = initVar(0)
    chan     = initVar(1)

    chan.exportImagesFlattened('C:\\prizmiq\\%s\\texture\\serverUp\\diffuse.jpg' % taskname)



main()
