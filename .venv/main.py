from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import DirectionalLight
import math
from panda3d.core import CardMaker, TextureStage

class MyApp(ShowBase):
    def __init__(self):
        # Call the superclass constructor
        ShowBase.__init__(self)

        base.disableMouse()

        self.add_background()

        # Load the model
        self.panda = self.loader.loadModel("models/panda")
        self.panda.reparentTo(self.render)
        self.panda.setPos(0, -10, -3)  # Adjust initial position closer to the camera
        self.panda.setScale(0.5, 0.5, 0.5)

        # Initial camera setup
        self.camera.set_pos(0, -20, 0)
        self.camera.look_at(0, 0, 0)

        # Add the task for movement
        self.taskMgr.add(self.move_panda, "MovePandaTask")

    def move_panda(self, task):
        time = task.time
        x = math.sin(time) * 2  # Sway gently along the x-axis
        y = -10 + time  # Move forward along the y-axis
        self.panda.setPos(x, y, -3)
        return Task.cont

    def add_background(self):
        cm = CardMaker("background")
        cm.setFrame(-10, 10, -10, 10)
        background = self.render.attachNewNode(cm.generate())
        background.setPos(0, 0, 0)

        bg_texture = self.loader.loadTexture("textures/forest.png")
        background.setTexture(bg_texture)

app = MyApp()
app.run()
