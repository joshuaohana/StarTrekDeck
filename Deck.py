from Player import Player
from Hand import Hand
class Deck(Player):
    def __init__(self, name, cardlist, shipcard):
        self.name = name
        self.cardlist = cardlist
        self.currentdiscard = []
        self.shipcard = shipcard
    def __str__(self):
        a=[]
        for card in self.cardlist:
            a.append(card.name)
        return 'Your deck has {} cards: {}'.format(len(self.cardlist), a)
    def drawhand(self):
        self.handname = Hand(self.name, self.playername + 'hand')
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

