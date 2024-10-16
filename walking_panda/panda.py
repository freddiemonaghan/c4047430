
from math import pi, sin, cos

from direct import task
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class WalkingPanda(ShowBase):
    def __init__(self, no_rotate=False, panda_scale=0.05, camera_distance=20, rotation_speed=6):
        ShowBase.__init__(self)
        # Load the environment model.
        self.no_rotate = no_rotate
        self.panda_scale = panda_scale
        self.camera_distance = camera_distance
        self.rotation_speed = rotation_speed

        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)


        # Add the spinCameraTask procedure to the task manager.
        if no_rotate == False: #if statement for no rotations
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")


        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(self.panda_scale, self.panda_scale, self.panda_scale)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * self.rotation_speed
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(self.camera_distance * sin(angleRadians), -self.camera_distance * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
