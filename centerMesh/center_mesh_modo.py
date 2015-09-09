import modo
import lx

def main():
	#partOne()
	partTwo()


#####################   PART ONE   #########################


def partOne():
	initScene()
	mesh   = initInputs(0)
	camera = initInputs(1)
	print mesh + '\n' + camera
	partOneMain(mesh, camera)

def initScene():
	scene = modo.Scene()

	scene.select(scene.items('mesh')[0])
	lx.eval('item.delete')

def initInputs(switch):
	scene = modo.Scene()

	mesh = str(scene.items('mesh'))
	mesh = mesh[12:19]

	camera = str(scene.item('Camera'))
	camera = camera[13:22]

	if switch == 0:
		return mesh
	elif switch == 1:
		return camera
	else:
		return scene


def partOneMain(mesh, camera):
	lx.eval('scene.open \"E:\\Prizmiq\\Shoes.com\\July\\New Balance W1980\\Geometry\\newBalanceW1980_zExport_v001.OBJ\" import')

	lx.eval('select.item %s add' % mesh)
	lx.eval('view3d.projection cam')
	lx.eval('view3d.cameraItem %s' % camera)
	lx.eval('camera.fit true false')


#####################   PART TWO   #########################


def partTwo():
	mesh   = initInputs(0)
	camera = initInputs(1)
	partTwoMain(mesh, camera)


def partTwoMain(mesh, camera):
	lx.eval('view3d.projection psp')
	lx.eval('select.item %s add' % mesh)
	lx.eval('center.bbox center')
	lx.eval('select.less')
	lx.eval('item.parent %s %s inPlace:1' % (mesh, camera))
	lx.eval('select.item %s add' % camera)
	lx.eval('transform.channel rot.X 0.0')
	lx.eval('transform.channel rot.Y 0.0')
	lx.eval('transform.channel rot.Z 0.0')
	lx.eval('select.item %s add' % mesh)
	lx.eval('transform.channel pos.X 0.0')
	lx.eval('transform.channel pos.Y 0.0')
	lx.eval('transform.channel pos.Z 0.0')

	lx.eval('select.convert vertex')
	lx.eval('select.vertex add 0 0')
	vert_index = lx.evalN('query layerservice verts ? selected')
	vert_posX = []
	vert_posY = []
	vert_posZ = []

	for element in vert_index:
		vert_pos_single = lx.eval('query layerservice vert.wpos ? ' + str(element))

		if not vert_pos_single[0] in vert_posX:
			vert_posX.append(vert_pos_single[0])
		if not vert_pos_single[1] in vert_posY:
			vert_posY.append(vert_pos_single[1])
		if not vert_pos_single[2] in vert_posZ:
			vert_posZ.append(vert_pos_single[2])

	vert_posX.sort()
	vert_posY.sort()
	vert_posZ.sort()

	if vert_posX[-1] > abs(vert_posX[0]):
		vert_posX = vert_posX[-1]
	else:
		vert_posX = abs(vert_posX[0])
	if vert_posY[-1] > abs(vert_posY[0]):
		vert_posY = vert_posY[-1]
	else:
		vert_posY = abs(vert_posY[0])
	if vert_posZ[-1] > abs(vert_posZ[0]):
		vert_posZ = vert_posZ[-1]
	else:
		vert_posZ = abs(vert_posZ[0])


	if vert_posX > vert_posY and vert_posX > vert_posZ:
		axisBig = vert_posX
	elif vert_posY > vert_posZ:
		axisBig = vert_posY
	else:
		axisBig = vert_posZ

	print axisBig

	lx.eval('select.typeFrom item;pivot;center;edge;polygon;vertex;ptag true')
	lx.eval('transform.channel scl.X %s' % (10/axisBig))
	lx.eval('transform.channel scl.Y %s' % (10/axisBig))
	lx.eval('transform.channel scl.Z %s' % (10/axisBig))




main()
