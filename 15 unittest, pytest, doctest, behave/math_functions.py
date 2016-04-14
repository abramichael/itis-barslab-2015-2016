import doctest

def zero(x):
    return 0

def fact(x):
    """
    >>> fact(4)
    24
    """
    if not isinstance(x, (int, long)):
        raise TypeError
    if x < 0:
        raise ValueError
    if x > 0:
        return reduce(lambda x, y: x * y, range(1, x + 1))
    elif x == 0:
        return 1

if __name__ == "__main__":
    doctest.testmod()
