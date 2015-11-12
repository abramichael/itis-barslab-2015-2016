from player import Player

class Game:
    def __init__(self, name1, name2):
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    def start(self):
        while (self.p1.isAlive() and self.p2.isAlive()):
            self.p1.kick(self.p2)
            if self.p2.isAlive():
                self.p2.kick(self.p1)


g = Game("MA", "Liya")
g.start()
