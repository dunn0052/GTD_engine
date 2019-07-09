import pygame as pg
from weapon import Weapon

class Mele(Weapon):

    def animate(self):
        if not self.attacking:
            pass
        else:
            if self.subFrame < self.frameSpeed:
                self.subFrame += self.frameCap
            else:
                self.hits()
                self.nextSpriteImage()
                self.subFrame = 0
                if self.currentImage == 0:
                    self.attacking = False
                    self.kill()

    def hits(self):
        for enem in self.level.enemy_sprites:
            if self.touching(enem):
                enem.hit(self.damage)

    def attack(self):
        self.attacking = True
