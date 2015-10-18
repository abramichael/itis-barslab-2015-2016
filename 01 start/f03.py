def sum(*args):
	s = 0
	for item in args:
		s += item
	return s

print sum(1,2,3)
print sum(100,200,100,100,500)
print sum(1)

a = (1,2,3,5,3)
print sum(*a)