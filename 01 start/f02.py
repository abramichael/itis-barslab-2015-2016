g = 9.86

def f(m):
	global g
	return m * g
	
x = 3
y = 5

print locals()
print globals()

print globals()['f'](5)

def f():
	x = 2
	y = 3
	print locals()
	print globals()
	
f()