import random
class Deck:
    #TODO make any instance of deck instantiate with an instance of Hand
    def __init__(self, name, allcards):
        self.name = name
        self.allcards = allcards
       # self.hand = Hand()

    def addcard(self, card):
        self.allcards.append(card)

    def trashcard(self, card_name, **args):
        deleted_count = 0

        for idx, card in enumerate(self.allcards):
            if args.get('count') is not 'all' and deleted_count >= args.get('count'): break
            if card.name is card_name:
                self.allcards.pop(idx)
                deleted_count += 1

        return 'You trashed ' + str(deleted_count) + ' copies of ' + card_name

    def shuffledeck(self):
        random.shuffle(allcards)
        return 'Your deck has been shuffled.'

    def changedeckname(self, newname):
        self.name = newname

    def print_deck(self):
        print('{}, {} cards'.format(self.name, len(self.allcards)))
        for card in self.allcards:
            print('*', card.name, '\n', card.flavortext)

    def count_cards(self):
        return "You have %s cards in deck %s" % (len(self.allcards), self.name)
