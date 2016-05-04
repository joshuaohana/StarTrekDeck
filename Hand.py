#TODO find a way to feed from Deck to here, an instance of Hand in Deck, an instance of Discardpile in Deck
from Deck import Deck
class Hand:
    def __init__(self,name, deck):
        self.name = name
        self.deck = deck
        self.currenthand = [self.deck.cardlist[0],self.deck.cardlist[1], self.deck.cardlist[2],
                            self.deck.cardlist[3], self.deck.cardlist[4]]
    def __str__(self):
        for card in self.currenthand:
            print(card.name)

    def calcstats(self):
        cardstats=[0,0,0,0]
        for card in self.currenthand:
            cardstats[0] += card.speed
            cardstats[1] += card.attack
            cardstats[2] += card.diplomacy
            cardstats[3] += card.shields
        return cardstats


#is this no longer relevant? Maybe?
    # def drawhand(self):
    #     while i < 5:
    #         i=0
    #         self.currenthand.append(Deck.cardlist[i])
    #         del(Deck.cardlist[i])
    #         i+=1

    def drawcard(self,card):
        currenthand.append(card)
    def discardhand(self):
        Discardpile.currentdiscard.append(currenthand)

        return cardstats
    def discard(self,card):
        return 'You discarded' + self.drawncards.pop(card)
    def trashcard(self, card_name, **args):
        deleted_count = 0
        for idx, card in enumerate(self.cardlist):
            if args.get('count') is not 'all' and deleted_count >= args.get('count'): break
            if card.name is card_name:
                self.allcards.pop(idx)
                deleted_count += 1