from panda3d.core import Vec3
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape

MAX_X_SPEED = 20
MAX_Y_SPEED = 20
MAX_Z_SPEED = 40

class MainChar():
    def __init__(self, asset='Assets/Blender_egg/gelo'):
        #Create character image and physics box
        shape = BulletBoxShape(Vec3(1, 1, 2))
        self.node = BulletRigidBodyNode('Box')
        self.node.setMass(1.0)
        self.node.addShape(shape)
        self.np = render.attachNewNode(self.node)
        self.model = loader.loadModel('Assets/Blender_egg/gelo')
        self.model.flattenLight()
        self.model.setColor(0.5,0.5,1,0)
        self.np.setPos(0, 0, 20)
        self.model.setPos(0, 0, -2)
        self.model.reparentTo(self.np)
    
    #Update movement state
    def UpdateKeyMap(self, key, state):
        self.keybDic[key] = state
    
    #Jump movement
    def Jump(self):
        self.speedZ = MAX_Z_SPEED


    def MovementSettings(self):
        #Possible keyboard inputs
        self.keybDic = {
            "up" : False,
            "down" : False,
            "left" : False,
            "right" : False,
        }

        #Speed attributes
        self.speedX = 0
        self.speedY = 0
        self.speedZ = 0

        #Set keyboard call functions
        self.accept("arrow_left", UpdateKeyMap, ["left", True])
        self.accept("arrow_left-up", UpdateKeyMap, ["left", False])
        
        self.accept("arrow_right", UpdateKeyMap, ["right", True])
        self.accept("arrow_right-up", UpdateKeyMap, ["right", False])
        
        self.accept("arrow_up", UpdateKeyMap, ["up", True])
        self.accept("arrow_up-up", UpdateKeyMap, ["up", False])
        
        self.accept("arrow_down", UpdateKeyMap, ["down", True])
        self.accept("arrow_down-up", UpdateKeyMap, ["down", False])


