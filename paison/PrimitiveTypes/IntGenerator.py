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
    #alternates bewteen positive and negative numbers in a natural sequence
    @staticmethod
    def naturalposneg():
        i = 0
        while True:
            yield i
            if i < 0:
                i = abs(i)
                i += 1
            else:
                i = -i
                i -= 1
       #yields a random number up to some maximum
    @staticmethod
    def randnum(maxn):
        import random
        while True:
            yield random.randrange(maxn)
     #random number generator where the max random changes everytime
    @staticmethod
    def superrandnum():
        import random
        maxn = random.randrange(3, 10)
        while True:
            yield random.randrange(2, maxn)
            maxn = random.randrange(maxn)
     #generates a sequence by continously dividing a number
    @staticmethod
    def divider(start, dividend):
        i = start
        while True:
            yield i
            i /= dividend

    @staticmethod
    def subtractor(start, sub):
        i = start
        while True:
            yield i
            i -= sub
