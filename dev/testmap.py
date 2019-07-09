# this is an example of a level system being created
# the creation functions are packed into a pickle file to be executed on load

from levelMaker import MapMaker
from enemy import Enemy

l = MapMaker(7, "palletTown")
l.packBackground("images//pkBG.png")
l.packTileSheet("images//BWBG.png", 80, 80)
l.packWallMap('maps//pkBg_Tile Layer 2.csv')
l.packTriggerMap('maps//pkBg_Tile Layer 5.csv')
l.packNpcMap('maps//pkBg_Tile Layer 4.csv')
l.packOverMap('maps//pkBg_Tile Layer 3.csv')
l.addRunningCommand(lambda:s.levelBuffer.addNpcDialogue(0, "This is some example text.\nHere is a new line.\nHere is another\nYou can press A to continue to the next screeen\nOr you can press A to get all of the text instantly\nOkay I am done talking"))
ene = lambda: Enemy(x = 300, y = 300, image = "images//csBig.png", frames = 12, cycle = 3, spd = 100, direction = 0, frameSpeed = 10, health = 10, level = s.levelBuffer)
l.packEnemy(ene)


l.addRunningCommand(lambda:s.levelBuffer.addExit("levels//ashHouseFirstFloor.pkl"))
l.addRunningCommand(lambda:s.levelBuffer.newLevel.TRIGGER_LAYER.get_sprite(0).setInteraction(lambda: s.nextLevel(0, 3, 8)))
l.saveLevel()
