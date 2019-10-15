import pygame as pg

class Lighting:
    def __init__(self, x, y, color = (0,0,0), alpha = 0):
        self.x = x
        self.y = y
        self.darkness = pg.Surface((self.x, self.y))
        self.darkness.fill(color)
        self.darkness.set_alpha(alpha)
