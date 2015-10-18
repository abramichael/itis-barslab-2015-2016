def f(x,y):
	return x + y
	
print f(1,2)
print f('a','b')
print f([1,2],[2,3])

d = {'a': 5, 'b': 10}
d['c'] = 15

for k in d.keys():
	print k, d[k]
	
for k,v in d.iteritems():
	print k, v