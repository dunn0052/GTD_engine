from newSprite import newSprite
import pygame as pg


class PC(newSprite):
    def __init__(self, x, y, image, spd, direction, frames, cycle, level = None, controller = None, frameSpeed = 100):
        self.level = level
        # Change to pc layer
        self.vx, self.vy = 0, 0
        self.x, self.y = x, y
        # CONSTANTS #
        self.SPEED = spd
        self.IMAGE = image
        # number of total frames in sprite sheet
        self.FRAMES = frames

        # which frame of animation in current cycle
        self.FRAME = 0

        # direction of PC
        self.DIRECTION = direction

        # how many frames per each cycle
        self.CYCLE = cycle

        # how long before next frame is called
        self.frameSpeed = frameSpeed


        # initialize the sprite instance

        self.moveFlag = False
        self.weapon = None

        self.up = 3
        self.down = 0
        self.left = 1
        self.right = 2



    def init(self):
        if self.IMAGE:
            super().__init__(self.IMAGE, self.FRAMES)
            self.hitbox = pg.Rect(self.x, self.y + self.rect.height/2, self.rect.width, self.rect.height/2)









    # can make it modular by setting a command dict

    def doDOWN(self):
        #  First dir
        self.changeDirection(self.down)
        self.vy = self.SPEED
        self.moveFlag = True

    def doLEFT(self):
        self.changeDirection(self.left)
        self.vx = -self.SPEED
        self.moveFlag = True

    def doRIGHT(self):
        self.changeDirection(self.right)
        self.vx = self.SPEED
        self.moveFlag = True

    def doUP(self):
        self.changeDirection(self.up)
        self.vy = -self.SPEED
        self.moveFlag = True



    def doL(self):
        if self.SPEED > 0:
            self.SPEED -= 50
        print(self.SPEED)

    def doR(self):
        if self.SPEED < 1500:
            self.SPEED += 50
        print(self.SPEED)

    def doA(self):
        if self.npcTrigger():
            if self.weapon:
                self.weapon.kill()
        else:
            if self.weapon:
                if not self.weapon.alive():
                    self.level.all_sprites.add(self.weapon)
                    self.level.animated_sprites.add(self.weapon)
                    self.level.PC_LAYER.add(self.weapon)
                self.weapon.update()
                self.weapon.attack()


    def doB(self):
        print("B")

    def doX(self):
        if self.weapon:
            self.weapon.kill()
        print("X")

    def doY(self):
        print("Y")

    def doSTART(self):
        print("START")

    def doSELECT(self):
        coords = (self.rect.x//self.level.tileWidth, self.rect.y//self.level.tileHeight)
        print(coords)


    def attatchWeapon(self, weapon):
        self.weapon = weapon
        self.weapon.update()



    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = self.collideHitbox(self.level.solid_sprites)
            if hits:
                if self.vx > 0:
                    self.x = hits.rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits.rect.right
                self.vx = 0
                self.rect.x = self.x
                self.hitbox.x = self.x
        if dir == 'y':
            hits = self.collideHitbox(self.level.solid_sprites)
            if hits:
                if self.vy > 0:
                    self.y = hits.rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits.rect.bottom - self.hitbox.height
                self.vy = 0
                self.rect.y = self.y
                self.hitbox.y = self.y + self.hitbox.height

    def solidTouching(self, layer):
        for ent in layer:
            if self.touching(ent):
                return [ent]

    def levelTrigger(self):
        trigger = self.collideHitbox(self.level.TRIGGER_LAYER)
        if trigger:
            trigger.interact()

    def npcTrigger(self):
            for npc in self.level.npc_sprites:
                if self.anySideCollision(npc.interactionRect):
                    npc.interact()
                    return True
            return False

    def anySideCollision(self, rectangle):
        # ugly but quick
        # interaction only when facing npc
        return (self.rect.collidepoint(rectangle.center[0], rectangle.top) and self.DIRECTION == 0) or (self.rect.collidepoint(rectangle.center[0], rectangle.bottom) and self.DIRECTION == 3) or (self.rect.collidepoint(rectangle.left, rectangle.center[1]) and self.DIRECTION == 2) or (self.rect.collidepoint(rectangle.right, rectangle.center[1]) and self.DIRECTION == 1)

    def movementUpdate(self):
        self.x += self.vx * self.level.dt
        self.y += self.vy * self.level.dt
        self.levelTrigger()
        self.rect.x = self.x
        self.hitbox.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.hitbox.y = self.y + self.hitbox.height
        self.collide_with_walls('y')
        # reset to starting position
        if not self.vx and not self.vy:
            self.changeImage(self.DIRECTION * self.CYCLE)
        self.vx, self.vy = 0,0

    def update(self):
        if self.moveFlag:
            self.movementUpdate()



    def changeDirection(self, direction):
        self.DIRECTION = direction
        self.changeImage(self.DIRECTION*self.CYCLE+self.FRAME)

    def moveTo(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.hitbox.x = self.x
        self.hitbox.y = self.y + self.hitbox.height

    def moveToTile(self, x, y):
        self.moveTo(x * self.level.tileWidth, y * self.level.tileHeight)


    def animate(self):
        if self.subFrame < self.frameSpeed:
            # 10ms is max animation speed
            self.subFrame += self.frameCap
        else:
            self.FRAME = (self.FRAME+1)%self.CYCLE              # Loop on end
            self.subFrame = 0



    def collideHitbox(self, group):
        for sprite in group:
            if sprite.rect.colliderect(self.hitbox):
                return sprite
