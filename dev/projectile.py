from newSprite import newSprite
import pygame as pg
class Projectile(newSprite):

    def __init__(self, x, y, image, speed = 0, time = 1000, frames = 1, damage = 0, frameSpeed = 0, missile = None):
        super().__init__(image, frames)
        self.missile = missile
        self.frames = frames
        self.frame = 0
        self.frameSpeed = frameSpeed
        self.speed = speed
        self.lifetime = time
        self.collided = False
        self.damage = damage
        self.speedy = 0
        self.speedx = 0

        self.up = 3
        self.down = 0
        self.left = 1
        self.right = 2

        self.rect.center = [x,y]

    def setDirection(self, direction):

        self.direction = direction

        if direction == self.up:
            self.speedy -= self.speed
            self.transform = 270
        elif direction == self.down:
            self.speedy += self.speed
            self.transform = 90
        elif direction == self.left:
            self.speedx -= self.speed
            self.transform = 180
        elif direction == self.right:
            self.speedx += self.speed
            self.transform = 0
        self.spawntime = pg.time.get_ticks()

    def update(self):
        if pg.time.get_ticks() - self.spawntime > self.lifetime:
            self.explode()

        if not self.collided:
            self.transformSprite(angle = self.transform, scale = 1)
            hit = self.groupTouching(self.missile.level.solid_sprites)
            if not hit:
                self.rect.centerx += self.speedx * self.missile.level.dt
                self.rect.centery += self.speedy * self.missile.level.dt
            else:
                if self.missile.level.enemy_sprites.has(hit):
                    hit.hit(self.damage)
                self.collided = True

    def animate(self):
        if self.collided:
            if self.subFrame < self.frameSpeed:
                # 10ms is max animation speed
                self.subFrame += self.frameCap
            else:
                self.subFrame = 0
                self.explode()

    def explode(self):
        if self.frame < self.frames:
            self.changeImage(self.frame)
            self.frame +=1
        else:
            self.finish()


    def finish(self):
        self.missile.attacking = False
        self.kill()
