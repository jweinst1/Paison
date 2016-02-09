#file that contains the dictionary generator

class DictionaryGenerator:
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    def __init__(self):
        self.previous = []
    def __repr__(self):
        return str(self.previous)
    def past(self):
        return str(self.previous)
    def emptydict(self):
        return '{}'
    def numberdict(self, length):
        return str({i:i for i in range(length)})
    def numberdictrandom(self, max, length):
        import random
        return str({i:random.randrange(max) for i in range(length)})
