from levelMaker import MapMaker


dome = MapMaker(8, "dome")
dome.packBackground("images//factoryBG.png")
dome.packTileSheet("images//ruins.png", 80, 80)
dome.packWallMap("maps//dome_Tile Layer 2.csv")
dome.packTriggerMap("maps//dome_Tile Layer 5.csv")
dome.packOverMap("maps//dome_Tile Layer 4.csv")
#dome.packLighting(50)
dome.addRunningCommand(lambda:s.levelBuffer.makeEnt(entType = "NPC", image = "images//chest.png", x = 20 , y = 11, frames = 2, interaction = (lambda: s.levelBuffer.newLevel.NPC_LAYER.get_sprite(0).changeImage(1))))
dome.addRunningCommand(lambda: s.levelBuffer.newLevel.NPC_LAYER.get_sprite(0).setText("Got 1 Nothing!"))
#dome.setLighting(50)
dome.saveLevel()
