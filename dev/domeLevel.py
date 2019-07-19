from levelMaker import MapMaker


dome = MapMaker(7, "dome")
dome.packBackground("images//factoryBG.png")
dome.packTileSheet("images//ruins.png", 80, 80)
dome.packWallMap("maps//dome_Tile Layer 2.csv")
dome.packTriggerMap("maps//dome_Tile Layer 5.csv")
dome.packOverMap("maps//dome_Tile Layer 4.csv")
dome.addRunningCommand(lambda:s.levelBuffer.makeEnt(entType = "NPC", image = "images//chest.png", x = 20 , y = 11, frames = 2, interaction = (lambda: s.levelBuffer.newLevel.NPC_LAYER.get_sprite(0).changeImage(1))))
#chest = Npc(x = 20, y = 11, image = "images//chest.png", frames = 2)
dome.addRunningCommand(lambda: s.levelBuffer.newLevel.NPC_LAYER.get_sprite(0).setText("Got 1 Nothing!"))
dome.saveLevel()
