a = 5
b = 10

#m = (a > b ? a : b) in Java, and now in Python:
m = a if a > b else b

#
print(reduce(lambda a,b: a if a > b else b, map(int, raw_input().split())))


