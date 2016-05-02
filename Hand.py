#TODO find a way to feed from Deck to here, an instance of Hand in Deck, an instance of Discardpile in Deck
from Deck import Deck
from Deck import cardlist
from CardTypes import shipcard
class Hand(Deck):
    currenthand = []
    #TODO drawhand will be a tough nut to crack
    def drawhand:
        while i < 5:
            i=0
            Deck.cardlist[i] = self.currenthand[i]
            Deck.cardlist.del[i]
            i+=1

    def drawcard(self,card):
        self.drawcard.append()
    def calculatestats:
        for card in Player.Hand:
            cardstats=[0,0,0,0]
            cardstats[0] += card.speed
            cardstats[1] += card.attack
            cardstats[2] += card.diplomacy
            cardstats[3]]+= card.shields
        return cardstats
    def discard(self,card):
        return 'You discarded' + self.drawncards.pop(card)