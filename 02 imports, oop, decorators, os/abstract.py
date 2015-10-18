import abc


class Animal:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def voice(self):
        pass

    def __str__(self):
        return "Animal"


class Dog(Animal):

    def voice(self):
        print "Hawk!"

a = Dog()
a.voice()
