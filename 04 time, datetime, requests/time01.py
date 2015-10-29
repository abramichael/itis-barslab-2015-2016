import time

def log_time(f):

    def wrapper(*args):
        time.clock()
        p = f(*args)
        print time.clock()
        return p
    return wrapper

@log_time
def fact(n):
    p = 1
    for i in xrange(n):
        p *= i + 1
    return p

print fact(20)