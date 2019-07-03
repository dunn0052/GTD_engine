from SCREEN import SCREEN
from BACKGROUND import Background
from level import Level
from controllerIO import Controller
from WALL import Wall

ctr = Controller(0)

# create the game object
s = SCREEN()

l = Level(backgroundImage = "images//pkBg.png", layerNum = 7, controller = ctr, spriteSheetPath = "images//BWBG.png", tileHeight = 80, tileWidth = 80)
l.makeEnt("PLAYER", "images//csBig.png", x = 200, y =350, spd = 500, frameSpeed = 50)
l2 = Level(backgroundImage = "images//house.png", layerNum = 7, controller = ctr, spriteSheetPath = "images//BWBG.png", tileHeight = 80, tileWidth = 80)
s.initLevel(l)
l.addExit(l2)
l2.addExit(l)
l.loadWalls('maps//pkBg_Tile Layer 2.csv')
l.loadTriggers('maps//pkBg_Tile Layer 5.csv')
l.loadNpcs('maps//pkBg_Tile Layer 4.csv')
l.loadOver('maps//pkBg_Tile Layer 3.csv')
l.NPC_LAYER.get_sprite(0).setInteraction(lambda: l.makeText())
l.makeEnt(entType = "ANIMATION", image = "images//wheel.png", x = 880, y = 1200, frames = 4, frameSpeed = 100)
l2.loadWalls('maps//house_Tile Layer 2.csv')
l2.loadTriggers('maps//house_Tile Layer 4.csv')
l2.loadNpcs('maps//house_Tile Layer 3.csv')
l.TRIGGER_LAYER.get_sprite(0).setInteraction(lambda: s.nextLevel(0, 288, 720))
l2.TRIGGER_LAYER.get_sprite(1).setInteraction(lambda: s.nextLevel(0, 498, 560))
l2.TRIGGER_LAYER.get_sprite(2).setInteraction(lambda: s.nextLevel(0, 498, 560))

s.setController(ctr)
s.run()
