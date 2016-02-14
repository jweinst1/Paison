#file for dealing with integers

class IntGenerators:
    #continously generates sequence of natural numbers
    @staticmethod
    def naturals():
        i = 0
        while True:
            yield i
            i += 1
    #continously generates sequence of even numbers
    @staticmethod
    def evens():
        i = 0
        while True:
            yield i
            i += 2

    @staticmethod
    def odds():
        i = 1
        while True:
            yield i
            i += 2
    #sequence based on specified interval
    @staticmethod
    def intervalsequence(inter):
        i = 0
        while True:
            yield i
            i += inter

    @staticmethod
    def negatives():
        i = 0
        while True:
            yield i
            i -= 1

    @staticmethod
    def powersoftwo():
        i = 2
        while True:
            yield i
            i *= 2

    @staticmethod
    def powersofnum(num):
        i = num
        while True:
            yield i
            i *= num
#continously generates the natural sum of numbers
    @staticmethod
    def naturalsum():
        i = 1
        while True:
            yield i
            i += i