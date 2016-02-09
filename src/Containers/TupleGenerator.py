#file that contains the tuple generator

class TupleGenerator:

    alphabet = list("abcdefghijklmnopqrstuvwxyz")


    def __init__(self):
        self.previous = []
    def __repr__(self):
        return str(self.previous)
    def past(self):
        return set(self.previous)
    def intlist(self, length):
        return str((elem for elem in range(length)))
    def intlisteven(self, length):
        return str((elem for elem in range(length) if elem%2==0))
    def intlistodd(self, length):
        return str((elem for elem in range(length) if elem%2!=0))
    def intlistreverse(self, length):
        lst = [elem for elem in range(length)]
        lst.reverse()
        return str(tuple(lst))
    def intdeeplist(self, length):
        return str(([elem] for elem in range(length)))
    def strlist(self, length):
        return str(('\"'+elem+'\"' for elem in TupleGenerator.alphabet))
    def strnumlist(self, length):
        return str(('\"'+str(elem)+'\"' for elem in range(length)))
    def intlistrandom(self, maxnum, length):
        import random
        return str((random.randrange(maxnum) for i in range(length)))
    def strlistrandom(self, length):
        import random
        return str(('\"'+random.choice(TupleGenerator.alphabet)+'\"' for i in range(length)))