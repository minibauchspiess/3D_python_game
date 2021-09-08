from panda3d.core import Vec3
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape
from solidObject import SolidObject

MAX_X_SPEED = 20
MAX_Y_SPEED = 20
MAX_Z_SPEED = 40

class MainChar():
    def __init__(self, asset='Assets/Blender_egg/gelo'):
        #Create character image and physics box
        self.box = SolidObject(asset, color=(0.5, 0.5, 1, 0), posAss=(0, 0, 2), dimBox=Vec3(1, 1, 2), weight=1.0, posBox=(0, 0, 20))
        
        self.MovementSettings()
    
    #Update movement state
    def UpdateKeyMap(self, key, state):
        self.keybDic[key] = state
    
    #Jump movement
    def Jump(self):
        self.speedZ = MAX_Z_SPEED


    def MovementSettings(self):
        #Possible keyboard inputs
        self.keybDic = {
            "up" : 0,
            "down" : 0,
            "left" : 0,
            "right" : 0,
            "jump" : 0
        }

        #Speed attributes
        self.speedX = 0
        self.speedY = 0
        self.speedZ = 0

        #Set keyboard call functions
        base.accept("arrow_left", self.UpdateKeyMap, ["left", MAX_X_SPEED])
        base.accept("arrow_left-up", self.UpdateKeyMap, ["left", 0])
        
        base.accept("arrow_right", self.UpdateKeyMap, ["right", MAX_X_SPEED])
        base.accept("arrow_right-up", self.UpdateKeyMap, ["right", 0])
        
        base.accept("arrow_up", self.UpdateKeyMap, ["up", MAX_Y_SPEED])
        base.accept("arrow_up-up", self.UpdateKeyMap, ["up", 0])
        
        base.accept("arrow_down", self.UpdateKeyMap, ["down", MAX_Y_SPEED])
        base.accept("arrow_down-up", self.UpdateKeyMap, ["down", 0])

        base.accept("space", self.UpdateKeyMap, ["jump", MAX_Z_SPEED])
        base.accept("space-up", self.UpdateKeyMap, ["jump", 0])
    
    def Update(self, dt):
        pos = self.box.np.getPos()
        pos.x += (self.keybDic["right"]-self.keybDic["left"])*dt
        pos.y += (self.keybDic["up"]-self.keybDic["down"])*dt
        pos.z += self.keybDic["jump"]*dt
        self.box.np.setPos( pos )


