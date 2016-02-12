#file that contains the variable name generator

class VarGenerator:
    modes = ["random", "syl"]
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    con = list("bcdfghjklmnpqrstvwxyz")
    vow = list("aeiou")

    def __init__(self, mode):
        assert mode in VarGenerator.modes
        self.previous = []
        self.mode = mode
    def __repr__(self):
        return str(self.previous)
    def __contains__(self, item):
        return item in self.past()
    def past(self):
        return set(self.previous)
    def genvar(self, length):
        import random
        if self.mode is "random":
            newvar = ""
            for i in range(length):
                newvar += random.choice(VarGenerator.alphabet)
            self.previous.append(newvar)
            return newvar
        else:
            newvar = ""
            for i in range(length//2):
                newvar += random.choice(VarGenerator.con) + random.choice(VarGenerator.vow)
            self.previous.append(newvar)
            return newvar


