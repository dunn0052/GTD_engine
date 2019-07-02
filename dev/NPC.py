from newSprite import newSprite
import pygame as pg
from textBox import Textbox

class Npc(newSprite):
    def __init__(self, x, y, image, interaction = None, level = None, frames = 1, interactionBuffer = 20, frameSpeed = 100):
        # bad idea to have a level reference
        self.groups = None
        self.level = level
        self.image = image
        self.frames = frames
        self.frameSpeed = frameSpeed
        # size of interaction buffer rect beyond image rect
        self.buffer = interactionBuffer
        super().__init__(self.image, self.frames)


        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y


        self.interaction = lambda:print(self.rect)

        # interaction rect
        self.interactionRect = pg.Rect((self.x - self.buffer, self.y - self.buffer), (self.originalWidth + self.buffer * 2, self.originalHeight + self.buffer * 2))
        if self.frames == 1:
            self.animate = self.noAnimate

    def noAnimate(self):
        pass

    def interact(self):
        self.interaction()

    def setInteraction(self, interaction):
        self.interaction = interaction

    def animate(self):
        if self.subFrame < self.frameSpeed:
            self.subFrame += self.frameCap
        else:
            self.nextSpriteImage()
            self.subFrame = 0
