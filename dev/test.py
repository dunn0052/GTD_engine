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
s.initLevel("levels//palletTown.pkl")
s.level.setPC(PC(image = "images//mog.png", x = 10, y =7, spd = 300, frameSpeed = 50, cycle = 3, direction = 0, frames = 12), x = 10 , y = 7 )

watergun = Missile(x = 0, y = 0, image = "images//waterGunOne.png", frames = 1, level = s.level, char = s.level.PC, damage = 1, frameSpeed = 30)

s.level.PC.attatchWeapon(watergun)
ene = Enemy(x = 0, y = 0, image = "images//csBig.png", frames = 12, cycle = 3, spd = 100, direction = 0, frameSpeed = 10, health = 10, level = s.level)
ene.move(300,300)
s.level.enemy_sprites.add(ene)
s.level.solid_sprites.add(ene)
s.level.NPC_LAYER.add(ene)
s.level.all_sprites.add(ene)
s.level.animated_sprites.add(ene)

s.run()
