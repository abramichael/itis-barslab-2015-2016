def fact(n):
    if not isinstance(n, (int, long)):
        raise TypeError("Needed INTEGER, Carl!")
    if n < 0:
        raise ValueError("n!, n > 0, Carl!")

    if n > 0:
        return n * fact(n-1)
    else:
        return 1

if __name__ == "__main__":
    print fact(5)
    print fact("abc")


