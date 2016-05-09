import card_data
from Deck import Deck
from Hand import Hand
from Discardpile import Discardpile
from Player import Player

class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    def battle (self, player1, player2):
        if [player1.hand.calcstats()] > player2.hand.calcstats[0]:
        elif player2.hand.calcstats[0] > player1.hand.calcstats[0]:
#TODO make this slice happen correctly - unclear on syntax


