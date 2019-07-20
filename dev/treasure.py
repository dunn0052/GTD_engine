from NPC import Npc

class Treasure(Npc):

    def putInTreasure(self, item, number = 1):
        self.contents = item
        # item class change __str__() to work with str()
        self.num = number
        self.empty = False

    def interact(self):
        if self.empty:
            self.level.displayText("Empty")
        else:
            self.nextSpriteImage()
            self.level.displayText("Got " + str(self.num) + " " + str(self.contents))
            self.empty = True
            return self.contents
