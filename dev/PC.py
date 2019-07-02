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
        # get first player
        # eventually set up a multi player mechanism
        self.controller = level.controllers[0]




    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.changeDirection(1)
            self.vx = -self.SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.changeDirection(2)
            self.vx = self.SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.changeDirection(3)
            self.vy = -self.SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.changeDirection(0)
            self.vy = self.SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
        if self.vx == 0 and self.vy == 0:
            self.changeImage(self.DIRECTION * self.CYCLE)

    def getButtonsPressed(self):
        self.buttons = self.controller.getInput()

        # can make it modular by setting a command dict
    def directionPadMove(self):
        c = self.controller
        moveFlag = False
        self.vx, self.vy = 0, 0
        if  c.DOWN in self.buttons:
            #  First dir
            self.changeDirection(0)
            self.vy = self.SPEED
            moveFlag = True

        if c.LEFT in self.buttons:
            self.changeDirection(1)
            self.vx = -self.SPEED
            moveFlag = True

        if c.RIGHT in self.buttons:
            self.changeDirection(2)
            self.vx = self.SPEED
            moveFlag = True

        if c.UP in self.buttons:
            self.changeDirection(3)
            self.vy = -self.SPEED
            moveFlag = True

        # diagnonals
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
        # default
        if self.vx == 0 and self.vy == 0:
            self.changeImage(self.DIRECTION * self.CYCLE)

        if moveFlag:
            self.movementUpdate()

    def buttonCommands(self, commands = None):
        c = self.controller
        if c.L in self.buttons:
            if self.SPEED > 0:
                self.SPEED -= 50
            print(self.SPEED)
        if c.R in self.buttons:
            if self.SPEED < 1500:
                self.SPEED += 50
            print(self.SPEED)
        if c.A in self.buttons:
            self.npcTrigger()

        if c.B in self.buttons:
            self.level.text.nextScreen()
        if c.X in self.buttons:
            print("X")
        if c.Y in self.buttons:
            print("Y")
        if c.START in self.buttons:
            print("START")
        if c.SELECT in self.buttons:
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

    def update(self):
        self.getButtonsPressed()
        self.directionPadMove()
        self.buttonCommands()




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
