Import Deck
#TODO feed an instance of deck into here
class Discardpile:
    def __init__(self, hand):
        self.hand = hand
    currentdiscard = []
    def shuffleintodeck:
        Deck.cardlist = Discardpile.currentdiscard
        Discardpile.currentdiscard = []
    def addcard(self, card):
        self.currentdiscard.append(card)