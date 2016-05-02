from Card import Card
class shipcard (Card):
    def __init__(self, name, stats):
        self.name=name
        self.stats = stats
    def printshipstats(self):
        print(list[self.stats])
