
# from random import shuffle

import card_data
from Deck import Deck
from Hand import Hand
import shipcard
from shipcard import shipcard




NicksDeck = Deck('Nick\'s Badass Mothafuckin Deck',[card_data.cards['Duras'], card_data.cards['Jean Luc Picard'], card_data.cards['Commander'], card_data.cards['Wesley Crusher'],
            card_data.cards['Warp Speed'], card_data.cards['Fire All Weapons'], card_data.cards['Commander'], card_data.cards['William Riker'],card_data.cards['Lieutenant'],card_data.cards['Ensign']])

#


Basicship= shipcard('Nick\'s Ship', 0, 0 ,0, 8)
NicksHand= Hand('Nicksfirsthand', NicksDeck, Basicship)
NicksHand.calcstats()


# print(NicksHand.currenthand)
# print(NicksHand)
#TODO giving me an error, but still doing what im telling it to do
# print(card_data.cards['Jean Luc Picard'].flavortext)
# NicksDeck.printdeck()
# print(NicksDeck.countdeck())
# NicksDeck.changedeckname('Nick\'s REALLY Badass Mothafuckin Deck')

# print(NicksHand.calcstats())
#TODO create a working instance of Player

# NicksDeck.addcard(Ensign)
# print(NicksDeck.count_cards())
# # fuck that ensign he sucks
# # you wanna use the name of the cards,
# #   since down the road you will no longer have a reference to the card item itself, but you'll always know its name
# print(NicksDeck.trashcard('Ensign', count='all'))
# print(NicksDeck.count_cards())
# print(NicksDeck.trashcard('Lieutenant', count=1))
# print(NicksDeck.count_cards())