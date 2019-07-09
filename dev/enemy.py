from newSprite import newSprite

class Enemy(newSprite):
    def __init__(self, x, y, image, frames, cycle, spd, direction, frameSpeed, health, level):
        self.health = health
        self.image = image
        self.frames = frames
        self.frameSpeed = frameSpeed
        self.level = level
        super().__init__(self.image, self.frames)


        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.DIRECTION = direction
        self.CYCLE = cycle
        self.FRAME = 0
        self.moveFlag = False
        self.changeDirection(self.DIRECTION)


    def changeDirection(self, direction):
        self.DIRECTION = direction
        self.changeImage(self.DIRECTION*self.CYCLE+self.FRAME)


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

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.level.solid_sprites)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.level.solid_sprites)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom - self.hitbox.height
                self.vy = 0
                self.rect.y = self.y


    def movementUpdate(self):
        self.x += self.vx * self.level.dt
        self.y += self.vy * self.level.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
        self.vx, self.vy = 0,0

    def update(self):
        if self.moveFlag:
            self.movementUpdate()

    def aStar(self):
        # do a* algorithm for path to PC
        pass


    def hit(self, damage):
        self.health -= damage
        print("hit!")
        if self.health < 1:
            print("killed")
            self.kill()


    def animate(self):
        if self.subFrame < self.frameSpeed:
            # 10ms is max animation speed
            self.subFrame += self.frameCap
        else:
            self.FRAME = (self.FRAME+1)%self.CYCLE              # Loop on end
            self.subFrame = 0
