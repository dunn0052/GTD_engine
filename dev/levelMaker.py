from level import Level
import objectRW

class LevelDesign:

    def __init__(self, backgroundImage = None, layerNum = 7, controller = None, spriteSheetPath = None, tileHeight = 0, tileWidth = 0):
        # create new level
        self.newLevel = Level(self, backgroundImage, layerNum, controller, spriteSheetPath, tileHeight, tileWidth)
