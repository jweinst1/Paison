#file that builds literal strings.

class StringGenerator:

    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    con = list("bcdfghjklmnpqrstvwxyz")
    vow = list("aeiou")
    num = list("0123456789")
    sym = list("~`!@#$%^&*()_+-=[]{}|;:<>?,.")
    allchar = alphabet + num + sym

    def __init__(self):
        self.previous = []
    def __repr__(self):
        return str(self.previous)
    def __contains__(self, item):
        return item in self.past()
    def past(self):
        return set(self.previous)
    def randstring(self, length):
        import random
        genstr = ''.join([random.choice(StringGenerator.allchar) for i in range(length)])
        return '\"'+genstr + '\"'
    def randalphabet(self, length):
        import random
        genstr = ''.join([random.choice(StringGenerator.alphabet) for i in range(length)])
        return '\"'+genstr + '\"'
    def randnumstr(self, length):
        import random
        genstr = ''.join([random.choice(StringGenerator.num) for i in range(length)])
        return '\"'+genstr + '\"'
    def randsymstr(self, length):
        import random
        genstr = ''.join([random.choice(StringGenerator.sym) for i in range(length)])
        return '\"'+genstr + '\"'


