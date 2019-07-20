from levelMaker import MapMaker
from treasure import Treasure
from enemy import Enemy

dome = MapMaker(7, "dome")
dome.packBackground("images//factoryBG.png")
dome.packTileSheet("images//ruins.png", 80, 80)
dome.packWallMap("maps//dome_Tile Layer 2.csv")
dome.packTriggerMap("maps//dome_Tile Layer 5.csv")
dome.packOverMap("maps//dome_Tile Layer 4.csv")
chest1 = Treasure(image = "images//chest.png", x = 20 , y = 11, frames = 2)
chest1.putInTreasure("test string")
dome.packSprite(chest1)

enemy = Enemy(x = 10, y = 5, image = "images//csBig.png", frames = 12, cycle = 3, spd = 100, direction = 0, frameSpeed = 10, health = 10)
dome.packSprite(enemy)

dome.saveLevel()
