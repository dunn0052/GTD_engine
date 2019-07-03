import pygame
from enum import Enum
from keyboardInput import KEYDICT as k
# get around rpi not having auto for some reason

try:
    from enum import auto
except ImportError:
    def auto():
        global number
        number += 1
        return number

# globals
POS = 0.9
NEG = -1.0
NUM_BUTTONS = 10
number = 0
# testing


class Controller:
    # number = controller number
    def __init__(self, number, keyboard = False):
        # button enums
        self.X = "X"
        self.A = "A"
        self.B = "B"
        self.Y = "Y"
        self.L = "L"
        self.R = "R"
        self.SELECT = "SELECT"
        self.START = "START"
        self.RIGHT = "RIGHT"
        self.LEFT = "LEFT"
        self.UP = "UP"
        self.DOWN = "DOWN"

        # fast access mapping from input to enum
        if keyboard:
            self.buttonMap = {k["x"]:self.X, k["a"]:self.A, k["b"]:self.B, k["y"]:self.Y, k["q"]:self.L, k["e"]:self.R, k["h"]:self.START, k["g"]:self.SELECT}
        else:
            self.buttonMap = {0:self.X, 1:self.A, 2:self.B, 3:self.Y, 4:self.L, 5:self.R, 8:self.SELECT, 9:self.START}

        self.buttonsPrev = set()


        # access joystick number
        try:
            #init joystick
            pygame.init()
            pygame.joystick.init()
            self.joystick = pygame.joystick.Joystick(number)
            self.joystick.init()
        except:
            print("No controller detected!")
            keyboard = True

        self.output = set()

        if keyboard:
            self.getInput = self.getKeys

        self.commands = None

    def setCommands(self, commands):
        self.commands = commands

    # get controller input
    def getInput(self):
        inputs = set()
        buttons = set()

        pygame.event.get()
        ## axis control ##
        for i in range( 2 ):
            axis = self.joystick.get_axis(i)
            if axis >= POS or axis == NEG:
                if axis > 0 and i == 0:
                    inputs.add(self.RIGHT)
                if axis < 0 and i == 0:
                    inputs.add(self.LEFT)
                if axis > 0 and i == 1:
                    inputs.add(self.DOWN)
                if axis < 0 and i == 1:
                    inputs.add(self.UP)

        for i in range(NUM_BUTTONS):
            button = self.joystick.get_button(i)
            if button == 1:
                buttons.add(self.buttonMap[i])
        newButtons = buttons - self.buttonsPrev
        self.buttonsPrev = set(buttons)
        return inputs.union(newButtons)

    def getKeys(self):
        inputs = set()
        buttons = set()

        pygame.event.clear()
        keys = pygame.key.get_pressed()
        # directional keys
        if sum(keys) > 0:
            if keys[k["up"]]:
                inputs.add(self.UP)
            if keys[k["down"]]:
                inputs.add(self.DOWN)
            if keys[k["left"]]:
                inputs.add(self.LEFT)
            if keys[k["right"]]:
                inputs.add(self.RIGHT)

            if keys[k["a"]]:
                buttons.add(self.A)
            if keys[k["s"]]:
                buttons.add(self.X)
            if keys[k["z"]]:
                buttons.add(self.B)
            if keys[k["x"]]:
                buttons.add(self.Y)
            if keys[k["q"]]:
                buttons.add(self.L)
            if keys[k["e"]]:
                buttons.add(self.R)
            if keys[k["f"]]:
                buttons.add(self.START)
            if keys[k["g"]]:
                buttons.add(self.SELECT)

        newButtons = buttons - self.buttonsPrev
        self.buttonsPrev = set(buttons)
        return inputs.union(newButtons)
