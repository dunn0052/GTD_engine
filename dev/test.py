from SCREEN import SCREEN
import objectRW
from controllerIO import Controller
from missile import Missile
from projectile import Projectile
from PC import PC
from enemy import Enemy

ctr = Controller(0)

# create the game object
s = SCREEN()
s.setController(ctr)
s.initLevel("levels//dome.pkl")
s.level.setPC(PC(image = "images//mog.png", x = 10, y =7, spd = 300, frameSpeed = 50, cycle = 3, direction = 0, frames = 12), x = 10 , y = 7 )

watergun = Missile(x = 0, y = 0, image = "images//waterGunOne.png", frames = 1, level = s.level, char = s.level.PC, damage = 1, frameSpeed = 30)

s.level.PC.attatchWeapon(watergun)

s.run()
