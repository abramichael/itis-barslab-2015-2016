# coding: utf-8

f = open("in.txt")
g = open("out.txt", "w")

eng_rus_dict = {}

for line in f:
    line = line.strip()
    k, v = line.split(" - ")
    print k.decode("utf-8"), v
    eng_words = v.split(", ")
    print eng_words
    for w in eng_words:
        if w not in eng_rus_dict:
            eng_rus_dict[w] = [k]
        else:
            eng_rus_dict[w].append(k)

for k, v in eng_rus_dict.iteritems():
    g.write("%s - %s\n" % (k, ", ".join(v)))

g.close()