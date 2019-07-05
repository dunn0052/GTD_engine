from newSprite import newSprite
import pygame as pg

class Weapon(newSprite):
    def __init__(self, x, y, image, level = None, frames = 1, damage = 0, frameSpeed = 0, char = None):
        # bad idea to have a level reference
        self.groups = None
        self.level = level
        self.image = image
        self.frames = frames
        self.frameSpeed = frameSpeed
        super().__init__(self.image, self.frames)

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.damage = damage
        self.speed = speed
        self.char = char
        self.currentFrame = 0

    def update(self):
        pass

    def animate(self):
        if self.subFrame < self.frameSpeed:
            self.subFrame += self.frameCap
        else:
            self.nextSpriteImage()
            self.subFrame = 0

    def attack():
        pass
