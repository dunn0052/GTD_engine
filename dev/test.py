from SCREEN import SCREEN
import objectRW
from controllerIO import Controller
ctr = Controller(0)

# create the game object
s = SCREEN()
s.setController(ctr)
l = objectRW.loadObject("levels//palletTown.pkl")
l2 = objectRW.loadObject("levels//ashHouseFirstFloor.pkl")

town = l.unpackLevel()
firstfloor = l2.unpackLevel()
s.initLevel(town)

s.run()
