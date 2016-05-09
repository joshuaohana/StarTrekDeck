#TODO wade through all these fuckin errors, including the Card to Shipcard module error -- clean this shit up
import os
import card_data
from Deck import Deck
from Hand import Hand
from CardTypes.shipcard import shipcard
from Discardpile import Discardpile
from Player import Player

NicksDeck = Deck('Nick\'s Badass Mothafuckin Deck',[card_data.cards['Ensign'], card_data.cards['Ensign'], card_data.cards['Ensign'], card_data.cards['Ensign'],
            card_data.cards['Ensign'], card_data.cards['Ensign'], card_data.cards['Commander'], card_data.cards['William Riker'],card_data.cards['Lieutenant'],card_data.cards['Ensign']])
Basicship= shipcard('Nick\'s Ship', 0, 0 ,0, 8)
NicksHand= Hand('Nick\'s first hand', NicksDeck, Basicship)
NicksDiscard = Discardpile(NicksHand)
PlayerNick = Player('Player Nick', NicksDeck, NicksHand, NicksDiscard, Basicship)

MaxinesDeck = Deck('Maxine\'s Wooftastic Deck', [card_data.cards['Duras'], card_data.cards['Jean Luc Picard'], card_data.cards['Commander'], card_data.cards['Jean Luc Picard'],
                card_data.cards['Warp Speed'], card_data.cards['Fire All Weapons'], card_data.cards['Commander'], card_data.cards['William Riker'],card_data.cards['Lieutenant'],card_data.cards['Ensign']])

PlayerNick.hand.calcstats()



# NicksDiscard.addhand(None)
# print(NicksDiscard)


#TODO giving me an error, but still doing what im telling it to do
# print(card_data.cards['Jean Luc Picard'].flavortext)
# NicksDeck.printdeck()
# print(NicksDeck.countdeck())
# NicksDeck.changedeckname('Nick\'s REALLY Badass Mothafuckin Deck')
# NicksHand.calcstats()

# print(NicksHand.calcstats())
#TODO create a working instance of Player
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