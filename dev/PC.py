from newSprite import newSprite
import pygame as pg


class PC(newSprite):
    def __init__(self, x, y, image, spd, direction, frames, cycle, level = None, controller = None, frameSpeed = 100):
        self.level = level
        # Change to pc layer
        self.vx, self.vy = 0, 0
        self.x = x
        self.y = y
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

        super().__init__(self.IMAGE, self.FRAMES)
        self.moveFlag = False






    # can make it modular by setting a command dict

    def doDOWN(self):
        #  First dir
        self.changeDirection(0)
        self.vy = self.SPEED
        self.moveFlag = True

    def doLEFT(self):
        self.changeDirection(1)
        self.vx = -self.SPEED
        self.moveFlag = True

    def doRIGHT(self):
        self.changeDirection(2)
        self.vx = self.SPEED
        self.moveFlag = True

    def doUP(self):
        self.changeDirection(3)
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
        self.npcTrigger()

    def doB(self):
        print("B")

    def doX(self):
        print("X")

    def doY(self):
        print("Y")

    def doSTART(self):
        print("START")

    def doSELECT(self):
        print(self.rect.topleft)





    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.level.solid_sprites, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.level.solid_sprites, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def solidTouching(self, layer):
        for ent in layer:
            if self.touching(ent):
                return [ent]

    def levelTrigger(self):
        for trigger in self.level.TRIGGER_LAYER:
            if self.checkCollision(trigger, center = True):
                trigger.interact()
                return

    def npcTrigger(self):
            for npc in self.level.NPC_LAYER:
                if self.anySideCollision(npc.interactionRect):
                    npc.interact()
                    return

    def anySideCollision(self, rectangle):
        # ugly but quick
        # interaction only when facing npc
        return (self.rect.collidepoint(rectangle.center[0], rectangle.top) and self.DIRECTION == 0) or (self.rect.collidepoint(rectangle.center[0], rectangle.bottom) and self.DIRECTION == 3) or (self.rect.collidepoint(rectangle.left, rectangle.center[1]) and self.DIRECTION == 2) or (self.rect.collidepoint(rectangle.right, rectangle.center[1]) and self.DIRECTION == 1)

    def movementUpdate(self):
        self.x += self.vx * self.level.dt
        self.y += self.vy * self.level.dt
        self.levelTrigger()
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
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

    def animate(self):
        if self.subFrame < self.frameSpeed:
            # 10ms is max animation speed
            self.subFrame += self.frameCap
        else:
            self.FRAME = (self.FRAME+1)%self.CYCLE              # Loop on end
            self.subFrame = 0
