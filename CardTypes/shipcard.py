class shipcard:
    def __init__(self, name, speed, attack, diplomacy, shields):
        self.name= name
        self.speed = speed
        self.attack = attack
        self.diplomacy = diplomacy
        self.shields = shields
    #TODO look up how properties work
    def __str__ (self):
        print('\'{}\''.format(self.name))
        if self.shields <= 8:
            print ('this ship sucks')
        if self.shields == 9:
            print ('this ship is ok')
        if self.shields == 10:
            print('this ship is p good')
        if self.shields >= 11:
            print ('this ship can fuck anybody, anytime')
        return 'It has {} speed, {} attack, {} diplomacy, and {} shields'.format(self.name,self.speed,self.attack,self.diplomacy,self.shields)
