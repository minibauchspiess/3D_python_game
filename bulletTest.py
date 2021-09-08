import direct.directbase.DirectStart
from panda3d.core import Vec3
from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape


base.cam.setPos(0, -10, 0)
base.cam.lookAt(0, 0, 0)

# World
world = BulletWorld()
world.setGravity(Vec3(0, 0, -9.81))

# Plane
shape = BulletBoxShape(Vec3(50, 50, 1))
node = BulletRigidBodyNode('Ground')
node.addShape(shape)
np = render.attachNewNode(node)
model = loader.loadModel('Assets/Blender_egg/ground')
model.setColor(0.3,0.5,0.3,0)
model.setPos(0,0,1)
np.setPos(0, 0, 0)
model.reparentTo(np)
world.attachRigidBody(node)

# Box
shape = BulletBoxShape(Vec3(1, 1, 2))
node = BulletRigidBodyNode('Box')
node.setMass(1.0)
node.addShape(shape)
np = render.attachNewNode(node)
model = loader.loadModel('Assets/Blender_egg/gelo')
model.flattenLight()
model.setColor(0.5,0.5,1,0)
np.setPos(0, 0, 20)
model.setPos(0, 0, -2)
model.reparentTo(np)
world.attachRigidBody(node)


def goLeft():
    pos = np.getPos()
    pos.x -= 10
    np.setPos(pos)

base.accept("space-up", goLeft)

# Update
def update(task):
    dt = globalClock.getDt()
    world.doPhysics(dt)
    return task.cont

taskMgr.add(update, 'update')
base.run()