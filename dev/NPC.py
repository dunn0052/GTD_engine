from newSprite import newSprite
import pygame as pg
from textBox import Textbox

class Npc(newSprite):
    def __init__(self, x, y, image, interaction = None, level = None, frames = 1, cycle = 3, spd = 100, interactionBuffer = 20, frameSpeed = 100):
        # bad idea to have a level reference
        self.groups = None
        self.level = level
        self.image = image
        self.frames = frames
        self.frameSpeed = frameSpeed
        # size of interaction buffer rect beyond image rect
        self.buffer = interactionBuffer
        self.rect = None
        self.interactionRect = None


        self.x = x
        self.y = y



        self.interaction = lambda:print(self.rect)

        # interaction rect
        # preset text
        self.text = None

        if self.frames == 1:
            self.animate = self.noAnimate

    def noAnimate(self):
        pass

    def interact(self):
        self.interaction()
        if self.text:
            self.level.displayText(self.text)

    def setInteraction(self, interaction):
        self.interaction = interaction

    def setText(self, text):
        self.text = text

    def animate(self):
        if self.subFrame < self.frameSpeed:
            self.subFrame += self.frameCap
        else:
            self.nextSpriteImage()
            self.subFrame = 0


    def moveTo(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.interactionRect = pg.Rect((self.x - self.buffer, self.y - self.buffer), (self.originalWidth + self.buffer * 2, self.originalHeight + self.buffer * 2))


    def moveToTile(self, x, y):
        self.moveTo(x * self.level.tileWidth, y * self.level.tileHeight)

    def unpackSprite(self):
        super().__init__(self.image, self.frames)
        self.interactionRect = pg.Rect((self.x - self.buffer, self.y - self.buffer), (self.originalWidth + self.buffer * 2, self.originalHeight + self.buffer * 2))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
