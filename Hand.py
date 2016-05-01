#TODO find a way to feed from Deck to here, an instance of Hand in Deck, an instance of Discardpile in Deck
from Deck import Deck
class Hand(Deck):
    #TODO drawhand will be a tough nut to crack
    # def drawhand(self,):
    def drawcard(self,card):
        self.drawcard.append(card)
    def discard(self,card):
        return 'You discarded' + self.drawncards.pop(card)