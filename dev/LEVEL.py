import pygame as pg
from textBox import Textbox
# the level class holds the layers of sprites to draw
# it also executes commands of the current controller context


class Level:
    def __init__(self, layerNum = 8, name = "NoName"):
        # controller access
        self.controllers = []
        self.tileHeight, self.tileWidth = 0,0
        # filenames
        self.name = name
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.solid_sprites = pg.sprite.Group()
        self.animated_sprites = pg.sprite.Group()
        self.static_sprites = pg.sprite.OrderedUpdates() # maybe layeredUpdates?
        self.text_layer = pg.sprite.GroupSingle()
        self.npc_sprites = pg.sprite.Group()
        self.enemy_sprites = pg.sprite.Group()
        self.lighting = None
        # draw layers
        self.layers = []
        for i in range(layerNum):
            self.layers.append(pg.sprite.LayeredUpdates())
        try:
            self.BACKGROUND = self.layers[0] # background image
            self.WALL_LAYER = self.layers[1] # level walls
            self.NPC_LAYER = self.layers[2] # draw NPC next
            self.TRIGGER_LAYER = self.layers[3]
            self.PC_LAYER = self.layers[4]
            self.OVER_LAYER = self.layers[5] # things overhead - bridges/roof
            ##self.WEATHER_LAYER = self.layers[6] # small alpha effects -- rain, clouds, etc.
        except:
            print("Number of layers must be greater than 8")

        self.exit = []
        self.dt = 0



    def doCommands(self, context):
        # get input
        buttons = self.controllers[0].getInput()
        for button in buttons:
            context.doCommand(button)

    def setController(self, controller):
        self.controllers.append(controller)

    def setControllerContext(self, context):
        self.context = context

    def setPC(self, PC, x, y):
        self.PC = PC
        self.PC.level = self
        self.PC_LAYER.add(self.PC)
        self.all_sprites.add(self.PC)
        self.animated_sprites.add(self.PC)
        self.PC.moveToTile(x, y)
        self.setControllerContext(self.PC)
        if self.PC.weapon:
            self.PC.weapon.kill()
            self.PC.weapon.level = self.PC.level

    def displayText(self, text):
        self.text = Textbox(text = text, backgroundImage = "images//textBackground.png", offset = 65, level = self)
        self.all_sprites.add(self.text)
        self.text_layer.add(self.text)
        self.setControllerContext(self.text)
