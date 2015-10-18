x1 = [1,2,41,7,2,7]
x2 = [1,5,2,7,2,4]

print sum(map(lambda x,y: x * y, x1, x2))

print reduce(lambda x,y: x + y, map(lambda x,y: x * y, x1, x2))

print filter(lambda x: x % 3 == 1, range(0, 50, 2))

#join
greetings = ["Hi", "Hello"]
s = "Bonjour"
if s not in greetings:
	greetings.append(s)
	
#print ", ".join(greetings)

print " ".join(map(lambda x: x + "!", greetings))