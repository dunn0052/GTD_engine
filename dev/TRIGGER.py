from newSprite import newSprite
import pygame as pg

class Trigger(newSprite):
    def __init__(self, x, y, height, width, interaction = lambda:print("Triggered"), transparent = False, level = None):
        # bad idea to have a level reference
        self.groups = None
        if level:
            self.level = level
            self.groups = self.level.all_sprites, self.level.TRIGGER_LAYER
            pg.sprite.Sprite.__init__(self, self.groups)
        else:
            pg.sprite.Sprite.__init__(self)

        if transparent:
            self.image = pg.Surface((width, height))
            self.image.set_colorkey((0,0,0))
        else:
            self.image = pg.Surface((width, height))
            self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.interaction = interaction
        if level:
            level.TRIGGER_LAYER.add(self)
            level.all_sprites.add(self)

    def interact(self):
        self.interaction()

    def setInteraction(self, interaction):
        self.interaction = interaction
