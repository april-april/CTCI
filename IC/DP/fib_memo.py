  class Fib_memo(object):

    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0:
            raise IndexError(
                'Index was negative. '
                'No such thing as a negative index in a series.'
            )

        # Base cases
        if n in [0, 1]:
            return n