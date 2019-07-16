from PC import PC
import objectRW as rw
import pygame as pg
pg.init()
pg.display.set_mode()
mog = PC(image = None, x = 0, y =0, spd = 300, frameSpeed = 50, cycle = 3, direction = 0, frames = 12)

rw.saveObject(mog, "chars//mog.pkl")
