from newSprite import newSprite
import pygame as pg

class Background(newSprite):
    def __init__(self, x, y, image = None, level = None, height = 0, width = 0 ):
        self.level = level
        if level:
            self.groups = self.level.all_sprites, self.level.BACKGROUND
        if image:
            super().__init__(image, 1)
        else:
            pg.sprite.Sprite.__init__(self)
            self.image = pg.Surface((height, width))
            self.image.fill((0,0,0))
            self.originalHeight = height
            self.originalWidth = width
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
