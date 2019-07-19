from weapon import Weapon
from projectile import Projectile
import pygame as pg
class Missile(Weapon):

    def animate(self):
        if not self.attacking:
            self.currentImage = 0
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

            projectile = self.projectile()
            projectile.setDirection(self.direction)
            self.level.all_sprites.add(projectile)
            self.level.animated_sprites.add(projectile)
            self.level.PC_LAYER.add(projectile)

            projectile.rect.centerx = self.rect.centerx + offsetX
            projectile.rect.centery = self.rect.centery + offsetY
            self.attacking = True

# class method
    def attack(self):
        self.shootProjectile()

    # image = "images//waterShot.png", speed = 800, time = 2000, frames = 3, damage = 2, frameSpeed = 10
    def setProjectile(self, projectile):
        self.projectile = projectile
