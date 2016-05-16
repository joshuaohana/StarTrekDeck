#TODO is import os a thing?
import card_data
from Player import Player
from Deck import Deck
from Hand import Hand
from CardTypes.shipcard import shipcard
from Discardpile import Discardpile


Basicship= shipcard('Nick\'s Ship', 0, 0 ,0, 8)
NicksDeck = Deck('Nick\'s Badass Mothafuckin Deck',[card_data.cards['Ensign'], card_data.cards['Ensign'], card_data.cards['Ensign'], card_data.cards['Ensign'],
            card_data.cards['Ensign'], card_data.cards['Ensign'], card_data.cards['Commander'], card_data.cards['William Riker'],card_data.cards['Lieutenant'],card_data.cards['Ensign']], Basicship)
PlayerNick = Player('Player Nick', NicksDeck, Basicship)

MaxinesDeck = Deck('Maxine\'s Wooftastic Deck', [card_data.cards['Duras'], card_data.cards['Jean Luc Picard'], card_data.cards['Commander'], card_data.cards['Jean Luc Picard'],
                card_data.cards['Warp Speed'], card_data.cards['Fire All Weapons'], card_data.cards['Commander'], card_data.cards['William Riker'],card_data.cards['Lieutenant'],card_data.cards['Ensign']], Basicship)
# MaxinesHand = Hand('Maxine\'s first hand', MaxinesDeck, Basicship)
# MaxinesDiscard = Discardpile(MaxinesHand)
PlayerMaxine = Player('Player Maxine', MaxinesDeck, Basicship)

print(NicksDeck.drawhand())

# NicksDiscard.addhand(None)
# print(NicksDiscard)


# print(card_data.cards['Jean Luc Picard'].flavortext)
# NicksDeck.printdeck()
# print(NicksDeck.countdeck())
# NicksDeck.changedeckname('Nick\'s REALLY Badass Mothafuckin Deck')
# NicksHand.calcstats()

# print(NicksHand.calcstats())
#TODO look for instances of self in drawcard

# NicksDeck.addcard(Ensign)
# print(NicksDeck.count_cards())
# # fuck that ensign he sucks
# # you wanna use the name of the cards,
# #   since down the road you will no longer have a reference to the card item itself, but you'll always know its name
# print(NicksDeck.trashcard('Ensign', count='all'))
# print(NicksDeck.count_cards())
# print(NicksDeck.trashcard('Lieutenant', count=1))
# print(NicksDeck.count_cards())