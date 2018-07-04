def fib(n):
    if n < 0:
        raise IndexError(
            'Index was negative. '
            'No such thing as a negative index in a series.'
        )
    elif n in [0, 1]:
        # Base cases
        return n

    print "computing fib(%i)" % n
    return fib(n - 1) + fib(n - 2)