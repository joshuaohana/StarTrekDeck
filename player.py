class Player:
    def __init__(self, playername, deck, hand, discardpile, shipcard):
        self.playername = playername
        self.deck = deck
        self.hand = hand
        self.discardpile = discardpile
        self.shipcard = shipcard
    missionpoints = 0
    if missionpoints >= 400:
        print(self.playername + 'wins')
    def __str__(self):
        return ('{} has deck "{}" and {} victory points'.format(self.playername, self.deck.name,self.missionpoints))
    # def battlestats:
    #     sum(self.Hand.['1'],self.Card['2'],self.card['3']
    # def playcard:
    # def playallcards:
    # def explore:
    # def buy:
    # def search:
    # def repair:



# these are all functions that represent what an instance of player could do on a turn