import pygame as pg
from Camera import Camera
import sys
from controllerOff import controllerOFF
from objectRW import loadObject

# the screen object represents the screen/hardware of the game system
# it draws the layers of each level and

class SCREEN:

    def __init__(self, Height = 1280, Width = 1920, fps = 120, refresh = 10, Title = "Cat Mystery Dungeon"):
        pg.init()
        self.width = Width
        self.height = Height
        self.screen = pg.display.set_mode()
        pg.display.set_caption(Title)
        self.clock = pg.time.Clock()
        self.controllers = []
        self.off = controllerOFF()
        # camera size of screen
        self.camera = Camera(Width, Height)

        # TIMING SETUP #
        self.FPS = fps
        self.REFRESH = refresh
        self.NEXT_FRAME = self.gameClock()
        self.screenRefresh = False
        self.tooSmall = False

    def initLevel(self, levelPath):
        self.levelBuffer = loadObject(levelPath)
        self.level = self.levelBuffer.unpackLevel()
        self.level.setController(self.controllers[0])
        self.camera.mapSize(self.level.background.originalHeight, self.level.background.originalWidth)
        if self.level.background.originalWidth < self.width or self.level.background.originalHeight < self.height:
            self.updateDisplay = self.updateDisplaySmall
        else:
            self.updateDisplay = self.updateDisplay

    def nextLevel(self, index, x, y):
        self.screenFade()
        PC = self.level.PC
        # remove from current sprite update
        self.level.PC.kill()
        # if an index
        if type(index) == type(1):
            self.initLevel(self.level.exit[index])
        # or if a path
        elif type(index) == type("a"):
            self.initLevel(index)
        # add same PC to next level
        self.level.setPC(PC, x, y)

    def screenFade(self):
        self.level.setControllerContext(self.off)
        fade = pg.Surface((self.width, self.height))
        fade.fill((0,0,0))
        for alpha in range(0, 100, 2):
            fade.set_alpha(alpha)
            self.screen.blit(fade, (0,0))
            pg.display.flip()
            pg.time.delay(10)

    def setController(self, controller, commands = None):
        self.controllers.append(controller)

    def doCommands(self):
        self.level.doCommands(self.level.context)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.level.dt = self.clock.tick(self.FPS) / 1000
            self.doCommands()
            self.update()
            self.updateDisplay()


    def update(self):
        # update portion of the game loop
        self.level.all_sprites.update()

        # multiplayer take the average of player coords?
        self.camera.update(self.level.PC)

    # redraw all sprites to screen
    def updateDisplay(self):
        # explore dirty sprites
        for layer in self.level.layers:
                self.drawScrollLayer(layer)
        self.level.static_sprites.draw(self.screen)
        self.level.text_layer.draw(self.screen)

        pg.display.flip()
        keys = pg.key.get_pressed()
        if (keys[pg.K_ESCAPE]):
            pg.quit()
            sys.exit()
        self.frameUpdate()

    def updateDisplaySmall(self):
        # needed if background too small
        self.screen.fill((0,0,0))
        # explore dirty sprites
        for layer in self.level.layers:
                self.drawScrollLayer(layer)
        self.level.static_sprites.draw(self.screen)
        self.level.text_layer.draw(self.screen)


        pg.display.flip()
        keys = pg.key.get_pressed()
        if (keys[pg.K_ESCAPE]):
            pg.quit()
            sys.exit()
        self.frameUpdate()

    def frameUpdate(self):
        # move next frame of animation
        if self.gameClock() > self.NEXT_FRAME:
            for sprite in self.level.animated_sprites:
                sprite.animate()
            self.NEXT_FRAME += self.REFRESH

    def gameClock(self):
        current_time = pg.time.get_ticks()
        return current_time

    # end program on esc -- otherwise update fames if needed
    def tick(self):
        pg.event.clear()
        keys = pg.key.get_pressed()
        if (keys[pg.K_ESCAPE]):
            self.quit()
        self.gameClock.tick(self.FPS)
        self.frameUpdate()
        return self.gameClock.get_fps()

    def drawScrollLayer(self, layer):
        for sprite in layer:
            # keep sprite pos static and draw with camera offsets
            self.screen.blit(sprite.image, self.camera.apply(sprite))

    def quit(self):
        pg.quit()
        sys.exit()
