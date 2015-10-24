from cw01 import fact

x = "abc"
try:
    y = fact(x)
except ValueError, e:
    print "ValueError of your function"
except TypeError, e:
    print "TypeError!!!"
else:
    print y
finally:
    print "- After all? - Always!"
