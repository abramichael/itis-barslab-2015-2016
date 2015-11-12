from subprocess import Popen

f = open("in.txt")

inp = map(lambda x: x.strip(), f.readlines())

filename = "generated.py"

g = open(filename, "w")

g.write("from %s import %s\n" % (inp[0], inp[1]))
g.write("f = open('%s', 'w')\n" % (inp[3]))
g.write("f.write(str(%s(%s)))\n" % (inp[1], inp[2]))
g.write("f.close()")
g.close()

p = Popen(["python", filename])