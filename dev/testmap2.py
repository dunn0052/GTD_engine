from levelMaker import MapMaker

l2 = MapMaker(7, "ashHouseFirstFloor")
l2.packBackground("images//house.png")
l2.packTileSheet("images//BWBG.png", 80, 80)
l2.packWallMap("maps//house_Tile Layer 2.csv")
l2.packNpcMap("maps//house_Tile Layer 3.csv")
l2.packTriggerMap("maps//house_Tile Layer 4.csv")
l2.addRunningCommand(lambda:s.levelBuffer.addExit("levels//palletTown.pkl"))
l2.addRunningCommand(lambda:s.levelBuffer.newLevel.TRIGGER_LAYER.get_sprite(1).setInteraction(lambda: s.nextLevel(0, 6, 7)))
l2.addRunningCommand(lambda:s.levelBuffer.newLevel.TRIGGER_LAYER.get_sprite(2).setInteraction(lambda: s.nextLevel(0, 6, 7)))
l2.saveLevel()
