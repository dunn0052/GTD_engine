import pygame, math, sys, os
vec = pygame.math.Vector2
class newSprite(pygame.sprite.Sprite):
    def __init__(self, image = None, frames=1):
      pygame.init()
      pygame.sprite.Sprite.__init__(self)
      self.images = []
      if type(image) == str:
          img = self.loadImage(image)
      else:
          img = image.convert_alpha()
      self.originalWidth = img.get_width() // frames
      self.originalHeight = img.get_height()
      frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
      x = 0
      for frameNo in range(frames):
          frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
          frameSurf.blit(img, (x, 0))
          self.images.append(frameSurf.copy())
          x -= self.originalWidth
      self.image = pygame.Surface.copy(self.images[0])

      self.screenRefresh = False
      self.currentImage = 0
      self.rect = self.image.get_rect()
      self.rect.topleft = (0, 0)
      self.mask = pygame.mask.from_surface(self.image)
      self.angle = 0
      self.scale = 1
      self.subFrame = 0
      # min ms of a frame
      self.frameCap = 10

      # commands
      self.commands = commands = {"A":self.doA,"B":self.doB,"X":self.doX,"Y":self.doY,"DOWN":self.doDOWN,"UP":self.doUP,"LEFT":self.doLEFT,"RIGHT":self.doRIGHT,"L":self.doL,"R":self.doR,"START":self.doSTART, "SELECT":self.doSELECT}



    def parseColour(self,colour):
      if type(colour) == str:
          # check to see if valid colour
          return pygame.Color(colour)
      else:
          colourRGB = pygame.Color("white")
          colourRGB.r = colour[0]
          colourRGB.g = colour[1]
          colourRGB.b = colour[2]
          return colourRGB

    def loadImage(self,fileName, useColorKey=False):
      if os.path.isfile(fileName):
          image = pygame.image.load(fileName)
          image = image.convert_alpha()
          # Return the image
          return image
      else:
          raise Exception("Error loading image: " + fileName + " - Check filename and path?")

    def addImage(self, filename):
      self.images.append(self.loadImage(filename))

    def move(self, xpos, ypos, centre=False):
      if centre:
          self.rect.center = [xpos, ypos]
      else:
          self.rect.topleft = [xpos, ypos]

    def changeImage(self, index):
      self.currentImage = index
      if self.angle == 0 and self.scale == 1:
          self.image = self.images[index]
      else:
          self.image = pygame.transform.rotozoom(self.images[self.currentImage], -self.angle, self.scale)
      oldcenter = self.rect.center
      self.rect = self.image.get_rect()
      originalRect = self.images[self.currentImage].get_rect()
      self.originalWidth = originalRect.width
      self.originalHeight = originalRect.height
      self.rect.center = oldcenter
      self.mask = pygame.mask.from_surface(self.image)
      if self.screenRefresh:
          pygame.display.update()

    def touching(self, other):
        collided = pygame.sprite.collide_mask(self , other)
        return collided

    def groupTouching(self, group):
        for sprite in group:
            if self.touching(sprite):
                return sprite

    def checkCollision(self, other, center = False):
        if center:
            return self.rect.collidepoint(other.rect.center)
        return self.rect.colliderect(other)

    def nextSpriteImage(self):
        self.currentImage += 1
        if self.currentImage > len(self.images) - 1:
            self.currentImage = 0
        self.changeImage(self.currentImage)


    def prevSpriteImage(self):
        self.currentImage -= 1
        if self.currentImage < 0:
            self.currentImage = len(self.images) - 1
        self.changeImage(self.currentImage)

    def transformSprite(self, angle, scale, hflip=False, vflip=False):
        oldmiddle = self.rect.center
        if hflip or vflip:
            tempImage = pygame.transform.flip(self.images[self.currentImage], hflip, vflip)
        else:
            tempImage = self.images[self.currentImage]
        if angle != 0 or scale != 1:
            self.angle = angle
            self.scale = scale
            tempImage = pygame.transform.rotozoom(tempImage, -angle, scale)
        self.image = tempImage
        self.rect = self.image.get_rect()
        self.rect.center = oldmiddle
        self.mask = pygame.mask.from_surface(self.image)
        if self.screenRefresh:
            pygame.display.update()



# virtual functions for button inputs
    def doCommand(self, button):
        self.commands[button]()

    def doA(self):
        pass
    def doB(self):
        pass
    def doX(self):
        pass
    def doY(self):
        pass
    def doLEFT(self):
        pass
    def doRIGHT(self):
        pass
    def doUP(self):
        pass
    def doDOWN(self):
        pass
    def doL(self):
        pass
    def doR(self):
        pass
    def doSTART(self):
        pass
    def doSELECT(self):
        pass

    def animate(self):
        pass

# unpack from pkling
    def unpackSprite(self):
        pass
