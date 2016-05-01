import random
from Player import Player
#making Deck a subclass of Player
class Deck(Player):
    #TODO make any instance of deck instantiate with an instance of Hand
    #TODO import battle system from previous project
    def __init__(self, name, cardlist):
        self.name = name
        self.cardlist = cardlist
       # self.hand = Hand()

    def addcard(self, card):
        self.allcards.append(card)

    def trashcard(self, card_name, **args):
        deleted_count = 0

        for idx, card in enumerate(self.cardlist):
            if args.get('count') is not 'all' and deleted_count >= args.get('count'): break
            if card.name is card_name:
                self.allcards.pop(idx)
                deleted_count += 1

        return 'You trashed ' + str(deleted_count) + ' copies of ' + card_name

    def shuffledeck(self):
        random.shuffle(cardlist)
        return 'Your deck has been shuffled.'

    def changedeckname(self, newname):
        self.name = newname

    def printdeck(self):
        print('{}, {} cards'.format(self.name, len(self.cardlist)))
        for card in self.cardlist:
            print('*', card.name, '\n', card.flavortext)

    def countdeck(self):
        return "You have {} cards in deck {}".format(len(self.cardlist), self.name)
