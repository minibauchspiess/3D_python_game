import direct.directbase.DirectStart
from panda3d.core import Vec3
from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape
from mainChar import MainChar
from solidObject import SolidObject

class Game():
    def __init__(self):
        self.base = base
        self.base.cam.setPos(0,-10,0)
        self.base.cam.lookAt(0, 0, 0)

        self.loadWorld()
        self.mainChar = MainChar()
        self.world.attachRigidBody(self.mainChar.box.node)
        
        taskMgr.add(self.update, 'update')
        base.run()

    
    def loadWorld(self):
        #Load world pyisics
        self.world = BulletWorld()
        self.world.setGravity(Vec3(0, 0, -9.81))

        #Load environment
            #Ground
        ground = SolidObject('Assets/Blender_egg/ground', color=(0.3,0.5,0.3,0), posAss=(0,0,1), dimBox=Vec3(50, 50, 1), weight=0, posBox=(0, 0, 0))
        self.world.attachRigidBody(ground.node)

    def update(self, task):
        dt = globalClock.getDt()
        self.mainChar.Update(dt)
        self.world.doPhysics(dt)
        return task.cont
    




# # World
# world = BulletWorld()

# # Plane

# # Box


# def goLeft():
#     pos = np.getPos()
#     pos.x -= 10
#     np.setPos(pos)

# base.accept("space-up", goLeft)

# # Update
# def update(task):
#     dt = globalClock.getDt()
#     world.doPhysics(dt)
#     return task.cont

# taskMgr.add(update, 'update')
# base.run()
game = Game()