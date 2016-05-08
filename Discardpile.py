import Deck
class Discardpile:
    currentdiscard = []
    def __init__(self, hand):
        self.hand = hand
    def __str__(self):
        return str(self.currentdiscard)
    def shuffleintodeck(self):
        Deck.cardlist = Discardpile.currentdiscard
        Discardpile.currentdiscard = []
    def addhand(self, nexthand):
        numberofhands = 0
        if numberofhands == 0:
            self.currentdiscard = self.hand
            numberofhands += 1
            return
        if numberofhands > 0:
            self.currentdiscard += nexthand
            numberofhands += 1