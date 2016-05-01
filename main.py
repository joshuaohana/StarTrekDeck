
# from random import shuffle

# I got it to print out my deck nicely with flavortext (make sure to look at Jean Luc), and addcard works.
# But I couldn't make the trashcard (line 19) or discard (line 35) methods work.
# Maybe it's .pop that I shouldn't be using. I also started on a Hand class (line 30),
# but couldn't quite figure out how to feed five cards from a Deck instance to a Hand instance.
# I also tried my best to make a shuffle method (line 22), but had zero success.
# If you find some time, I would appreciate any feedback. Thanks again.


from Deck import Deck
from Hand import Hand
from Card import Card
import card_data



print(card_data.cards['JeanLucPicard'].flavortext)
NicksDeck = Deck('Nick\'s Badass Mothafuckin Deck', [card_data.cards['Duras'], card_data.cards['JeanLucPicard']])
# NicksDeck.changedeckname('Nick\'s REALLY Badass Mothafuckin Deck')

# NicksDeck.print_deck()

print(NicksDeck.count_cards())
# NicksDeck.addcard(Ensign)
# print(NicksDeck.count_cards())
# # fuck that ensign he sucks
# # you wanna use the name of the cards,
# #   since down the road you will no longer have a reference to the card item itself, but you'll always know its name
# print(NicksDeck.trashcard('Ensign', count='all'))
# print(NicksDeck.count_cards())
# print(NicksDeck.trashcard('Lieutenant', count=1))
# print(NicksDeck.count_cards())