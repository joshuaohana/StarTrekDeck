
from Player import Player
from CardTypes.shipcard import shipcard
from Deck import Deck
class Hand(Deck):
    def __init__(self,name):
        self.name = name
        self.currenthand = [self.deck.cardlist[0],self.deck.cardlist[1], self.deck.cardlist[2],
                            self.deck.cardlist[3], self.deck.cardlist[4]]

#TODO make an instantiation of hand remove top five cards from deck, need to make it work w/ the super
    def updatedeck(self):
        if 1==1:
            del super.cardlist[0:4]
    def __str__(self):
        return 'You have {}, {}, {}, {}, and {}'.format(self.currenthand[0].name, self.currenthand[1].name,
                                                    self.currenthand[2].name, self.currenthand[3].name, self.currenthand[4].name)
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
    @staticmethod
    def battle(player1, player2):
        p1stats = player1.hand.calcstats()
        p2stats = player2.hand.calcstats()
        if p1stats['speed'] > p2stats['speed']:
            while p1stats['shields'] > 0 and p2stats['shields'] > 0:
                p2stats['shields'] -= p1stats['attack']
                if p1stats['shields'] > 0 and p2stats['shields'] > 0:
                    p1stats['shields'] -= p2stats['attack']
        elif p2stats['speed'] > p1stats['speed']:
            while p1stats['shields'] > 0 and p2stats['shields'] > 0:
                p1stats['shields'] -= p2stats['attack']
                if p1stats['shields'] > 0 and p2stats['shields'] > 0:
                    p1stats['shields'] -= p2stats['attack']
        elif p2stats['speed'] == p1stats['speed']:
            while p1stats['shields'] > 0 and p2stats['shields'] > 0:
                p2stats['shields'] -= p1stats['attack']
                p1stats['shields'] -= p2stats['attack']
        if p1stats['shields'] <= 0 and p2stats['shields'] <= 0:
            player2.currenthand.append(card_data.cards['Ensign'])
            player1.currenthand.append(card_data.cards['Ensign'])
            print('Both Players Lose. Womp.')
        if p1stats['shields'] <= 0:
            player1.hand.currenthand.append(card_data.cards['Ensign'])
            print('{} wins! {} can suck a dick and take an Ensign!'.format(player2.playername, player1.playername))
        if p2stats['shields'] <= 0:
            player2.hand.currenthand.append(card_data.cards['Ensign'])
            print('{} wins! {} can take a Ensign and fuck outta here!'.format(player1.playername, player2,playername))

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
            if args.get('count') is not 'all' and deleted_count >= args.get('count'):
                break
            if card.name is card_name:
                self.allcards.pop(idx)
                deleted_count += 1
        return 'You trashed ' + str(deleted_count) + ' copies of ' + card_name
