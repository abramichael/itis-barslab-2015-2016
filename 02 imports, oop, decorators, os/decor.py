def eat_well(bread):

    def decor(f):

        def wrapper():
            print bread + " BREAD"
            f()
            print bread + " BREAD"

        return wrapper

    return decor


@eat_well(bread="BLACK")
def eat():
    print "MEAT"


eat()
