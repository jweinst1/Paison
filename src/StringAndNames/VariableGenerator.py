#file that contains the variable name generator

class VarGenerator:
    modes = ["random", "syl"]
    alphabet = "abcdefghijklmnopqrstuvwxyz".split("")
    con = "bcdfghjklmnpqrstvwxyz".split("")
    vow = "aeiou".split("")

    def __init__(self, mode):
        assert mode in VarGenerator.modes
        self.previous = []
        self.mode = mode
    def __repr__(self):
        return str(self.previous)
    def vars(self):
        return set(self.previous)
    def genvar(self, length):
        import random
        if self.mode is "random":
            newvar = ""
            for i in range(length):
                newvar += random.choice(VarGenerator.alphabet)
            return newvar
        else:
            newvar = ""
            for i in range(length//2):
                newvar += random.choice(VarGenerator.con) + random.choice(VarGenerator.vow)
            return newvar


