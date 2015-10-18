from random import randrange


class Phone:
    n = 0

    @staticmethod
    def printN():
       print Phone.n

    @classmethod
    def f(cls):
        print dir(cls)

    def __init__(self, model="Nokia"):
        Phone.n += 1
        self.model = model
        self.__serial = randrange(100000)

    def __str__(self):
        return "%s/%s" % (self.model, self.__serial)

    def call(self):
        print "Din-din! Who is it?"

    def work(self):
        self.call()


class Camera:
    def __init__(self, model='Canon'):
        self.model = model
        self.__serial = randrange(100000)

    def make_photo(self):
        print "making photo"

    def work(self):
        self.make_photo()

class SmartPhone(Phone, Camera):
    def __init__(self, model='HTC'):
        #super(model)
        Phone.__init__(self, model)


#p = Phone()
#print str(p) + "!"
#print p._Phone__serial
#p.call()

#sp = SmartPhone()
#print sp
#sp.work()

p1 = Phone()
p2 = Phone()
print p1.n
print p2.n
print Phone.n
#Phone.n = 3
p1.n = 4
Phone.n = 5
print p1.n
print Phone.n
print p2.n
Phone.printN()