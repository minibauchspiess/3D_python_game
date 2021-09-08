from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import NodePath
from panda3d.physics import ActorNode
from panda3d.physics import ForceNode
from panda3d.physics import LinearVectorForce
# import direct.directbase.DirectStart
from panda3d.core import Vec3
from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape




keyMap = {
    "up" : False,
    "down" : False,
    "left" : False,
    "right" : False
}

def UpdateKeyMap(key, state):
    keyMap[key] = state

class MyGame(ShowBase):
    def __init__(self):
        super().__init__()

        self.enableParticles()

        # World
        self.world = BulletWorld()
        self.world.setGravity(Vec3(0, 0, -9.81))

        # Ground
        self.ground = self.loader.loadModel("Assets/Blender_egg/ground")
        node = BulletRigidBodyNode('Ground')
        node.addShape(self.ground)
        np = self.render.attachNewNode(node)
        np.setPos(0, 0, -2)
        self.world.attachRigidBody(node)

        # Ice
        node = BulletRigidBodyNode('Box')
        node.setMass(1.0)
        node.addShape(self.gelo)
        np = self.render.attachNewNode(node)
        np.setPos(0, 0, 2)
        self.world.attachRigidBody(node)
        self.gelo = self.loader.loadModel('Assets/Blender_egg/gelo')
        self.gelo.flattenLight()
        self.gelo.reparentTo(np)

        # node = NodePath("PhysicsNode")
        # node.reparentTo(self.render)
        # an = ActorNode("jetpack-guy-physics")
        # anp = node.attachNewNode(an)
        # self.physicsMgr.attachPhysicalNode(an)

        # self.gelo = self.loader.loadModel("Assets/Blender_egg/gelo")
        # self.gelo.setPos(0,50,100)
        # self.gelo.setColor(0.5,0.5,1,0)
        # self.gelo.reparentTo(anp)

        # an.getPhysicsObject().setMass(136.077)

        # gravityFN=ForceNode('world-forces')
        # gravityFNP=self.render.attachNewNode(gravityFN)
        # gravityForce=LinearVectorForce(0,0,-9.81) #gravity acceleration
        # gravityFN.addForce(gravityForce)

        # self.physicsMgr.addLinearForce(gravityForce)

        
        # node1 = NodePath("PhysicsNode")
        # node1.reparentTo(self.render)
        # an1 = ActorNode("jetpack-guy-physics")
        # anp1 = node.attachNewNode(an1)
        # self.physicsMgr.attachPhysicalNode(an1)

        

        

        self.speed = 2
        self.jumpSpeed = 10

        self.accept("arrow_left", UpdateKeyMap, ["left", True])
        self.accept("arrow_left-up", UpdateKeyMap, ["left", False])
        
        self.accept("arrow_right", UpdateKeyMap, ["right", True])
        self.accept("arrow_right-up", UpdateKeyMap, ["right", False])
        
        self.accept("arrow_up", UpdateKeyMap, ["up", True])
        self.accept("arrow_up-up", UpdateKeyMap, ["up", False])
        
        self.accept("arrow_down", UpdateKeyMap, ["down", True])
        self.accept("arrow_down-up", UpdateKeyMap, ["down", False])
        
        self.accept("space-up", self.jump)

        self.taskMgr.add(self.Update, "update")

    def jump(self):
        pos = self.gelo.getPos()
        pos.z += self.jumpSpeed
        self.gelo.setPos(pos)

    def Update(self, task):
        dt = globalClock.getDt()

        pos = self.gelo.getPos()

        if keyMap["down"]:
            pos.y -= self.speed*dt*100
        if keyMap["up"]:
            pos.y += self.speed*dt
        if keyMap["left"]:
            pos.x -= self.speed*dt
        if keyMap["right"]:
            pos.x += self.speed*dt

        self.gelo.setPos(pos)

        self.world.doPhysics(dt)

        return task.cont

game = MyGame()
game.run()