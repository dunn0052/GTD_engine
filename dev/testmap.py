from levelMaker import MapMaker

l = MapMaker(7, "palletTown")
l.setBackground("images//pkBG.png")
l.setTileSheet("images//BWBG.png", 80, 80)
l.setWallMap('maps//pkBg_Tile Layer 2.csv')
l.setTriggerMap('maps//pkBg_Tile Layer 5.csv')
l.setNpcMap('maps//pkBg_Tile Layer 4.csv')
l.setOverMap('maps//pkBg_Tile Layer 3.csv')
l.setPCMap(image = "images//csBig.png", x = 200, y =350, spd = 500, frameSpeed = 50, cycle = 3, direction = 0, frames = 12)
l.addRunningCommand(lambda:l.addNpcDialogue(0, "This is some example text.\nHere is a new line.\nHere is another\nYou can press A to continue to the next screeen\nOr you can press A to get all of the text instantly\nOkay I am done talking"))


l2 = MapMaker(7, "ashHouseFirstFloor")
l2.setBackground("images//house.png")
l2.setTileSheet("images//BWBG.png", 80, 80)
l2.setWallMap("maps//house_Tile Layer 2.csv")
l2.setNpcMap("maps//house_Tile Layer 3.csv")
l2.setTriggerMap("maps//house_Tile Layer 4.csv")

l.addRunningCommand(lambda:l.addExit(l2.newLevel))
l2.addRunningCommand(lambda:l2.addExit(l.newLevel))
l.addRunningCommand(lambda:l.newLevel.TRIGGER_LAYER.get_sprite(0).setInteraction(lambda: s.nextLevel(0, 288, 720)))
l2.addRunningCommand(lambda:l2.newLevel.TRIGGER_LAYER.get_sprite(1).setInteraction(lambda: s.nextLevel(0, 498, 560)))
l2.addRunningCommand(lambda:l2.newLevel.TRIGGER_LAYER.get_sprite(2).setInteraction(lambda: s.nextLevel(0, 498, 560)))

l.saveLevel()
l2.saveLevel()
