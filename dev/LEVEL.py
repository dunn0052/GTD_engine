from PC import PC
from BACKGROUND import Background
import WALL
import NPC
import TRIGGER
import over
import mele
from textBox import Textbox
import pygame as pg
from controllerIO import Controller as ct
from functools import partial
from spritesheet import spritesheet
import csv
import os


class LEVEL:
    def __init__(self, backgroundImage = None, layerNum = 7, controller = None, spriteSheetPath = None, tileHeight = 0, tileWidth = 0):

        # controller access
        self.controllers = []
        if controller:
            self.controllers.append(controller)
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.solid_sprites = pg.sprite.Group()
        self.animated_sprites = pg.sprite.Group()
        self.static_sprites = pg.sprite.OrderedUpdates() # maybe layeredUpdates?
        self.text_layer = pg.sprite.GroupSingle()
        # draw layers
        self.layers = []
        for i in range(layerNum):
            self.layers.append(pg.sprite.LayeredUpdates())
        try:
            self.BACKGROUND = self.layers[0] # background image
            self.WALL_LAYER = self.layers[1] # level walls
            self.NPC_LAYER = self.layers[2] # draw NPC next
            self.TRIGGER_LAYER = self.layers[3]
            self.layers[4] = pg.sprite.GroupSingle()
            self.PC_LAYER = self.layers[4]
            self.OVER_LAYER = self.layers[5] # things overhead - bridges/roof
            self.WEATHER_LAYER = self.layers[6] # small alpha effects -- rain, clouds, etc..
        except:
            print("Number of layers must be greater than 7")

        if backgroundImage:
            self.background = Background(x = 0, y = 0, image = backgroundImage)
        else:
            self.background = Background(x = 0, y = 0, level = self, height = 10000, width = 19200)

        self.BACKGROUND.add(self.background)
        self.all_sprites.add(self.background)
        self.exit = []
        self.dt = 0

        # for sprite sheet
        if spriteSheetPath:
            self.tileHeight = tileHeight
            self.tileWidth =  tileWidth
            self.sheet = spritesheet(spriteSheetPath, tileHeight, tileWidth)
            self.tiles = self.sheet.get_tiles()

    def getInput(self):
        self.PC.getButtonsPressed(self.controllers[0])

    def setPC(self, PC, x, y):
        self.PC = PC
        self.PC.level = self
        self.PC_LAYER.add(PC)
        self.all_sprites.add(PC)
        self.PC.moveTo(x, y)


    def addExit(self,level):
        self.exit.append(level)


# factory for game objects
    def makeEnt(self, entType, image = None, x = 0, y = 0, frames = 12, direction = 1, cycle = 3, spd = 200, interaction = None, frameSpeed = 100):
        entType = entType.upper()
        if entType == "WALL":
            entity = WALL.Wall(x, y, image)
            self.all_sprites.add(entity)
            self.WALL_LAYER.add(entity)
        elif entType == "PLAYER":
            entity = PC(x, y, image, spd, direction, frames, cycle, level = self, frameSpeed = frameSpeed)
            self.all_sprites.add(entity)
            self.animated_sprites.add(entity)
            self.PC_LAYER.add(entity)
            self.PC = entity
            self.PC.moveTo(x, y)
        elif entType == "NPC":
            entity = NPC.Npc(image, x, y, frames, direction, cycle, spd, level = self)
            self.all_sprites.add(entity)
            self.NPC_LAYER.add(entity)
        elif entType == "TRIGGER":
            entity = TRIGGER.Trigger(x, y, 64,64, interact = interaction, transparent = True, level = self)
            self.all_sprites.add(entity)
            self.TRIGGER_LAYER.add(entity)
        elif entType == "ANIMATION":
            entity = NPC.Npc(image = image, x = x, y = y, frames = frames, level = self)
            self.all_sprites.add(entity)
            self.NPC_LAYER.add(entity)
            self.animated_sprites.add(entity)
            self.solid_sprites.add(entity)
        elif entType == "MELE":
            entity = mele.Mele(image = image, x = x, y = y, frames = frames, frameSpeed = 10)
            self.all_sprites.add(entity)
            self.NPC_LAYER.add(entity)



    # Level has a map class to help design levels
    def loadData(self, filename):
        data = []
        if filename.endswith(".txt"):
            with open(filename, 'rt') as f:
                for line in f:
                    data.append(line.strip())
        elif filename.endswith(".csv"):
            with open(filename, 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    data.append(row)
        return data

    def loadWalls(self, filename):
        data = self.loadData(filename)
        for row, tiles in enumerate(data):
                    for col, tile in enumerate(tiles):
                        if int(tile) > -1:
                            ent = WALL.Wall(x = col * self.tileHeight, y = row * self.tileWidth, image = self.tiles[int(tile)])
                            self.WALL_LAYER.add(ent)
                            self.all_sprites.add(ent)
                            self.solid_sprites.add(ent)

    def loadTriggers(self, filename):
        data = self.loadData(filename)
        for row, tiles in enumerate(data):
                    for col, tile in enumerate(tiles):
                        if int(tile) > -1:
                            ent = TRIGGER.Trigger(x = col * self.tileHeight, y = row * self.tileWidth, height = self.tileHeight, width = self.tileWidth, transparent = True)
                            self.TRIGGER_LAYER.add(ent)
                            self.all_sprites.add(ent)

    def loadNpcs(self, filename):
        data = self.loadData(filename)
        for row, tiles in enumerate(data):
                    for col, tile in enumerate(tiles):
                        if int(tile) > -1:
                            ent = NPC.Npc(x = col * self.tileHeight, y = row * self.tileWidth, image = self.tiles[int(tile)], level = self)
                            self.NPC_LAYER.add(ent)
                            self.all_sprites.add(ent)
                            self.solid_sprites.add(ent)

    def loadOver(self, filename):
        data = self.loadData(filename)
        for row, tiles in enumerate(data):
                    for col, tile in enumerate(tiles):
                        if int(tile) > -1:
                            ent = over.Over(x = col * self.tileHeight, y = row * self.tileWidth, image = self.tiles[int(tile)])
                            self.OVER_LAYER.add(ent)
                            self.all_sprites.add(ent)

    def makeText(self):
        sampleText = "NPC: This is a really long sentence with a couple of breaks.\nSometimes it will break even if there isn't a break " \
        "in the sentence, but that's because the text is too long to fit the screen.\nIt can look strange sometimes.\n" \
        "You can press B to clear the text screen and begin writing the new text." \
        "When the text finally finishes, the screen will be killed and a new screen can continue. \n I should have the NPC name begin at every new screen." \
        "\n I don't know, but I will check out Chrono Trigger or whatever to see what they do."
        self.text = Textbox(text = sampleText)
        self.all_sprites.add(self.text)
        self.text_layer.add(self.text)
