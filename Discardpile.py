Import Deck
class Discardpile(Deck):
    currentdiscard = []
    def shuffleintodeck:
        Deck.cardlist = Discardpile.currentdiscard
        Discardpile.currentdiscard = []
