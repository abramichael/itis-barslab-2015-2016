def f(x):
	return x * x
	
g = f

print g(2)

def super_f(f,x):
	return f(x)
	
print super_f(int, 5.8)
print super_f(abs, -5)
print super_f(f, 4)
print super_f(lambda x: x % 3, 10)

u = lambda x,y: x * y
#def u(x,y)
#	return x * y

print (lambda x,y: x * y)(2,3)