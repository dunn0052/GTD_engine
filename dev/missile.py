from weapon import Weapon
from projectile import Projectile
import pygame as pg
class Missile(Weapon):

    def animate(self):
        if not self.attacking:
            self.currentImage = 0
            pass
        else:
            if self.subFrame < self.frameSpeed:
                self.subFrame += self.frameCap
            else:
                #self.nextSpriteImage()
                self.subFrame = 0
                if self.currentImage == 0:
                    self.attacking = False


    def shootProjectile(self):
        if not self.attacking:
            d = self.direction
            offsetX, offsetY = 0,0
            if d == self.char.up:
                offsetY = -self.rect.h
            elif d == self.char.down:
                offsetY = self.rect.h
            elif d == self.char.left:
                offsetX = -self.rect.w
            elif d == self.char.right:
                offsetX = self.rect.w

            shot = Projectile(x = self.rect.centerx + offsetX, y = self.rect.centery + offsetY, image = "images//waterShot.png", speed = 800, direction = self.char.DIRECTION, time = 2000, frames = 3, damage = 2, frameSpeed = 10,  missile = self, level = self.level)
            self.attacking = True

    def attack(self):
        self.shootProjectile()
