from Deck import Deck
class Card(Deck):
    def __init__(self, name, speed, attack, diplomacy, shields, cost, value, missionpoints, specialeffect, flavortext):
        self.name = name
        self.speed = speed
        self.attack = attack
        self.diplomacy = diplomacy
        self.shields = shields
        self.cost = cost
        self.value = value
        self.missionpoints = missionpoints
        self.specialeffect = specialeffect
        self.flavortext = flavortext