#file that builds literal strings.

class StringGenerator:

    alphabet = "abcdefghijklmnopqrstuvwxyz".split("")
    con = "bcdfghjklmnpqrstvwxyz".split("")
    vow = "aeiou".split("")
    num = "0123456789".split("")
    sym = "~`!@#$%^&*()_+-=[]{}|;:<>?,."

    def __init__(self):
        self.previous = []
    def __repr__(self):
        return str(self.previous)
    def __contains__(self, item):
        return item in self.past()
    def past(self):
        return set(self.previous)


