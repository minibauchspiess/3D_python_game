from panda3d.core import Vec3
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape

MAX_X_SPEED = 20
MAX_Y_SPEED = 20
MAX_Z_SPEED = 40

class SolidObject():
    def __init__(self, asset, color, posAss, dimBox, weight, posBox, physics=True):
        self.model = self.addModel(asset, color, posAss)
        if physics:
            self.node, self.np = self.addPhysicsBox(dimBox, weight, posBox)
            self.model.reparentTo(self.np)


    def addModel(self, asset, color, pos):
        # Create model, edit it (color, position..) and return it
        model = loader.loadModel(asset)
        model.setColor(color)
        model.setPos(pos)
        return model
    
    def addPhysicsBox(self, dim, mass, pos):
        shape = BulletBoxShape(dim)
        node = BulletRigidBodyNode('Box')
        node.setMass(mass)
        node.addShape(shape)
        np = render.attachNewNode(node)
        np.setPos(pos)
        return node, np
    
