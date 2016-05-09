from Deck import Deck
from CardTypes.shipcard import shipcard
class Hand(Deck):
    def __init__(self,name, deck, shipcard):
        self.name = name
        self.deck = deck
        self.currenthand = [self.deck.cardlist[0],self.deck.cardlist[1], self.deck.cardlist[2],
                            self.deck.cardlist[3], self.deck.cardlist[4]]
        self.shipcard = shipcard
#TODO make an instantiation of hand remove top five cards from deck, need to make it work w/ the super
    def updatedeck(self):
        if 1==1:
            del super.cardlist[0:4]
    def __str__(self):
        return 'You have {}, {}, {}, {}, and {}'.format(self.currenthand[0].name, self.currenthand[1].name,
                                                    self.currenthand[2].name, self.currenthand[3].name, self.currenthand[4].name)
#TODO make __str__ not as messy when it prints
    def calcstats(self):
        cardstats = {
            'speed': self.shipcard.speed,
            'attack': self.shipcard.attack,
            'diplomacy': self.shipcard.diplomacy,
            'shields': self.shipcard.shields}

        for card in self.currenthand:
            cardstats['speed'] += card.speed
            cardstats['attack'] += card.attack
            cardstats['diplomacy'] += card.diplomacy
            cardstats['shields'] += card.shields
        return cardstats
#TODO read some articles on self
#TODO clean shit up
#is this no longer relevant? Maybe?
    # def drawhand(self):
    #     while i < 5:
    #         i=0
    #         self.currenthand.append(Deck.cardlist[i])
    #         del(Deck.cardlist[i])
    #         i+=1


    def drawcard(self,card):
        self.currenthand.append(card)
    def discardhand(self):
        Discardpile.currentdiscard.append(currenthand)
#TODO fix this -- Discardpile is not functioning

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
        return 'You trashed ' + str(deleted_count) + ' copies of ' + card_name
