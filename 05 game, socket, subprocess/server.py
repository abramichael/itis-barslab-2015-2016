from player import Player
import random
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 1234              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr

player_name = "Rustem"
p = Player(player_name)
enemy = Player("enemy")
while True:
    data = int(conn.recv(4))
    if data == 0:
        print "%s missed" % enemy.name
    else:
        print "%s kicked %s" % (enemy.name, p.name)
        p.hp -= data
        print "%s hp is %s" % (p.name, p.hp)

    x = int(raw_input(player_name + ">"))
    pr = 0.7 - (x - 1) * 0.65 / 8
    rand_value = random.random()
    #print "%s : %s" % (rand_value, pr)
    if rand_value < pr:
        print "%s kicked %s" % (p.name, enemy.name)
        conn.sendall(str(x))
        enemy.hp -= x
        print "%s hp is %s" % (enemy.name, enemy.hp)
    else:
        print "%s missed" % p.name
        conn.sendall(str(0))




while 1:
    data = conn.recv(1024)
    print data
    conn.sendall(data)
conn.close()