import re

#non-named example
#p = re.compile(r"([01]\d|2[0-3]):([0-5]\d)")
#named example
p = re.compile(r"(?P<hours>[01]\d|2[0-3]):(?P<minutes>[0-5]\d)")

s = "Today we have class at 16:00, and later on 20:30."

for item in re.finditer(p, s):

    #print "FOUND: " + item.group(0)
    #print item.group(1)
    #print item.group(2)

    print "FOUND: " + item.group()
    print item.group("minutes")
    print item.group("hours")