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
mog = objectRW.loadObject("chars//mog.pkl")
mog.unpackSprite()
s.level.setPC(mog, x = 10 , y = 7 )

watergun = objectRW.loadObject("weapons//watergun.pkl")
watergun.unpackSprite()
s.level.PC.attatchWeapon(watergun)

s.run()
