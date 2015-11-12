import random
import socket
from player import Player

HOST = '10.17.9.85'    # The remote host
PORT = 1234              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
player_name = "Azat"
p = Player(player_name)
enemy = Player("enemy")
while True:
    x = int(raw_input(player_name + ">"))
    pr = 0.7 - (x - 1) * 0.65 / 8
    rand_value = random.random()
    #print "%s : %s" % (rand_value, pr)
    if rand_value < pr:
        print "%s kicked %s" % (p.name, enemy.name)
        s.sendall(str(x))
        enemy.hp -= x
        print "%s hp is %s" % (enemy.name, enemy.hp)
    else:
        print "%s missed" % p.name
        s.sendall(str(0))

    data = int(s.recv(4))
    if data == 0:
        print "%s missed" % enemy.name
    else:
        print "%s kicked %s" % (enemy.name, p.name)
        p.hp -= data
        print "%s hp is %s" % (p.name, p.hp)

s.close()