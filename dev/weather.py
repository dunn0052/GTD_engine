from newSprite import newSprite
import pygame as pg

class Weather(newSprite):
    def __init__(self, x, y, image):
        self.image = image
        super().__init__(self.image, 1)

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def addDarkness(self, alpha, color = (0,0,0)):
        self.darkness = pg.Surface(self.image.x, self.image.y)
        self.darkness.fill(color)
        self.darkness.set_alpha(alpha)

    def draw(screen):
        screen.blit(self.darkness)
        
