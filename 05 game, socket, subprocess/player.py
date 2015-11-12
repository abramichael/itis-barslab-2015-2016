import random

class Player:

    def getP(self, x):
        return 0.7 - (x - 1) * 0.65 / 8

    def __init__(self, name):
        self.name = name
        self.hp = 50

    def isAlive(self):
        return self.hp > 0

    def kick(self, p):
        x = int(raw_input(self.name + ">"))
        pr = self.getP(x)
        rand_value = random.random()
        #print "%s : %s" % (rand_value, pr)
        if rand_value < pr:
            print "%s kicked %s" % (self.name, p.name)
            p.hp -= x
            print "%s hp is %s" % (p.name, p.hp)
        else:
            print "%s missed" % self.name
