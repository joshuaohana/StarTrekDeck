
# from random import shuffle

# I got it to print out my deck nicely with flavortext (make sure to look at Jean Luc), and addcard works.
# But I couldn't make the trashcard (line 19) or discard (line 35) methods work.
# Maybe it's .pop that I shouldn't be using. I also started on a Hand class (line 30),
#   but couldn't quite figure out how to feed five cards from a Deck instance to a Hand instance.
# I also tried my best to make a shuffle method (line 22), but had zero success.
#   If you find some time, I would appreciate any feedback. Thanks again.


class Card:
    def __init__(self, name, speed, attack, diplomacy, shields, cost, value, specialeffect, flavortext):
        self.name = name
        self.speed = speed
        self.attack = attack
        self.diplomacy = diplomacy
        self.shields = shields
        self.cost = cost
        self.value = value
        self.specialeffect = specialeffect
        self.flavortext = flavortext


class Deck:
    def __init__(self, name, allcards):
        self.name = name
        self.allcards = allcards

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
        self.allcards.random.shuffle(allcards)
        return 'Your deck has been shuffled.'

    def changedeckname(self, newname):
        self.name = newname

    def print_deck(self):
        print('{}, {} cards'.format(self.name, len(self.allcards)))
        for card in self.allcards:
            print('*', card.name, '\n', card.flavortext)

    def count_cards(self):
        return "You have %s cards in deck %s" % (len(self.allcards), self.name)

class Hand:
    def __init__(self, drawncards):
        self.drawncards = drawncards

    def drawcard(self,card):
        self.drawncards.append(card)

    def discard(self,card):
        return 'You discarded' + self.drawncards.pop(card)

Duras = Card('Duras',0, 3, 1, 0, 7, 0,'You may trash 1 card in your hand or move 1 card from your hand to the top of another player\'s deck.', '"You would dare to insult my father\'s name?"')

WesleyCrusher = Card('Wesley Crusher',1, 0, 1, 0, 4, 0, 'You get +1 search.\nDuring your turn, you may upgrade this card to a\nFederation Character from starbase with a cost 8 or less.',
                     '"I\'m with Starfleet. We don\'t lie."')

GeordiLaForge = Card('Geordi La Forge', 2,2,0,'Amount of damage that was removed\nfrom your flagship this turn +2.', 7,0,
                     'Remove up to 2 damage from your flagship.','"I need to get down to engineering and begin that analysis."')

Data = Card('Data',2,2,0,0,7,0,'Draw 2 cards. Move 2 cards from your hand to the\ntop of your deck in any order.', '"My programming may be inadequate to the task."')

NatashaYar = Card('Natasha Yar',0, 2, 0, 0, 5, 0, 'You may upgrade 1 Maneuver in your hand or bridgeto a Maneuver from starbase costing up to 2 more.', '"As Security Chief, I can\'t just stand here..."')

WilliamRiker = Card('William Riker',2,2,2,0,8,0,'Select 1 opponent. If you do, name a card.\nThat opponent must guess if you have that card in your hand.\nIf they guess wrong, you may have them peek at your hand,\nand you draw 2 cards.',
                    '"Poker...is that a game of some sort?"')

Sela = Card('Sela',2,2,2,0,9,0, 'Name 1 card. Peek at each opponent\'s hand. If they have that card in their hand,\nthey must discard 1 copy of it.',
            '"Humans have a way of showing up\nwhen you least expect them."')

BeverlyCrusher = Card('Beverly Crusher',1,0,2,0,5,0,'Move up to 2 Characters from your discard area\nto the top of your deck in any order.', '"I\'d like you to come to Sick Bay for some examinations."')

Worf = Card('Worf',0,2,0,0,6,0,'You may upgrade 1 Maneuver or Setup in your hand or bridge\nto a Maneuver or Setup from starbase costing up to 2 more and move it to your hand.',
            '"Klingons don\'t laugh."')

JeanLucPicard = Card('Jean Luc The Pussy Slayer',2,2,3,0,9,0, 'When you complete a Mission or diplomacy\na Starship, you may gain 1 card from starbase.', '"I think you\'ve got a great deal\nto learn from Starfleet...\nand my dick."')

FireAllWeapons = Card('Fire All Weapons', 0,7,0,0,7,0, None, 'FIRE ZE MISSILES')

WarpSpeed = Card('Warp Speed',5,0,0,0,6,0, 'You may discard 1 card from your hand.\nIf you do, draw 1 card.', '"I wanna go fast" -Ricky Bobby')

DeannaTroi = Card('Deanna Troi',1,0,2,0,6,0,'Peek at 1 opponent\'s hand. Select 1 Character\n in their hand with a cost of 7 or less\nand they discard it.', '"You must have know I couldn\'t allow you to do that."')

Ensign = Card('Ensign',0,1,0,0,1,1,'+1 XP', 'The bottom of the foodchain.')

Lieutenant = Card('Lieutenant',1,0,0,0,3,2,'+2 XP', 'Better than an Ensign.')

Commander = Card('Commander',1,1,0,0,5,3,'+3 XP', 'Now we\'re talkin!')


NicksDeck = Deck('Nick\'s Badass Mothafuckin Deck', [Duras, WesleyCrusher, GeordiLaForge, Data, NatashaYar, WilliamRiker, Sela, BeverlyCrusher, Worf, JeanLucPicard,FireAllWeapons,WarpSpeed,DeannaTroi,Ensign,Ensign,Ensign,Lieutenant,Lieutenant,Lieutenant,Commander,Commander])
# NicksDeck.changedeckname('Nick\'s REALLY Badass Mothafuckin Deck')

# NicksDeck.print_deck()

print NicksDeck.count_cards()
NicksDeck.addcard(Ensign)
print NicksDeck.count_cards()
# fuck that ensign he sucks
# you wanna use the name of the cards,
#   since down the road you will no longer have a reference to the card item itself, but you'll always know its name
print NicksDeck.trashcard('Ensign', count='all')
print NicksDeck.count_cards()
print NicksDeck.trashcard('Lieutenant', count=1)
print NicksDeck.count_cards()