#TODO find a way to feed from Deck to here, an instance of Hand in Deck, an instance of Discardpile in Deck
class Hand:
    def drawcard(self,card):
        self.drawcard.append(card)
    def discard(self,card):
        return 'You discarded' + self.drawncards.pop(card)