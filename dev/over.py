from newSprite import newSprite
import pygame as pg

class Over(newSprite):
    def __init__(self, x, y, image):
        self.image = image
        super().__init__(self.image, 1)

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
