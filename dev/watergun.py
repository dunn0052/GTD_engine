from missile import Missile
from projectile import Projectile
import objectRW as rw
watergun = Missile(x = 0, y = 0, image = "images//waterGunOne.png", frames = 1, damage = 1, frameSpeed = 30)
watershot = lambda: Projectile(x = 0, y = 0, image = "images//waterShot.png", speed = 800, time = 2000, frames = 3, damage = 2, frameSpeed = 10,  missile = watergun)
watergun.setProjectile(watershot)

rw.saveObject(watergun, "weapons//watergun.pkl")
