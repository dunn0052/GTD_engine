from newSprite import newSprite
import pygame as pg

class Weapon(newSprite):
    def __init__(self, x, y, image, speed = 0, frames = 1, damage = 0, frameSpeed = 0):
        self.image = image
        self.frames = frames
        self.frameSpeed = frameSpeed
        self.rect = None
        self.x = x
        self.y = y

        self.damage = damage
        self.speed = speed
        self.currentFrame = 0
        self.attacking = False
        self.direction = 0

    def setChar(self, char):
        self.char = char

    def update(self):
        # move with PC and change direction when called
        if self.char.DIRECTION == self.char.down:
            self.transformSprite(angle = 90, scale = 1)
            self.rect.center = (self.char.rect.centerx, self.char.rect.centery + self.rect.h)
            self.direction = self.char.down
        if self.char.DIRECTION == self.char.left:
            self.transformSprite(angle = 180, scale = 1, vflip = True)
            self.rect.center = (self.char.rect.centerx - self.rect.w , self.char.rect.centery)
            self.direction = self.char.left
        if self.char.DIRECTION == self.char.right:
            self.transformSprite(angle = 0, scale = 1)
            self.rect.center = (self.char.rect.centerx + self.rect.w , self.char.rect.centery)
            self.direction = self.char.right
        if self.char.DIRECTION == self.char.up:
            self.transformSprite(angle = 270, scale = 1)
            self.rect.center = (self.char.rect.centerx, self.char.rect.centery - self.rect.w)
            self.direction = self.char.up

    def animate(self):
        pass

    def unpackSprite(self):
        super().__init__(self.image, self.frames)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def setLevel(self, level):
        self.level = level
