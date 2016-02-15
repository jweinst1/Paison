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

    #produces stream of alphabetically oriented letters
    def alpharange(self, length):
        newstr = ""
        for i in range(length):
            newstr += StringGenerator.alphabet[i % 25]
        return '\"'+ newstr + '\"'
    def randstring(self, length):
        import random
        genstr = ''.join([random.choice(StringGenerator.allchar) for i in range(length)])
        return '\"'+genstr + '\"'
    def randalphabet(self, length):
        import random
        genstr = ''.join([random.choice(StringGenerator.alphabet) for i in range(length)])
        return '\"'+genstr + '\"'
    def randalphaspacestr(self, length):
        import random
        genstr = ''.join([random.choice(StringGenerator.alphabet) + " " for i in range(length//2)])
        return '\"'+genstr + '\"'
    def randnumstr(self, length):
        import random
        genstr = ''.join([random.choice(StringGenerator.num) for i in range(length)])
        return '\"'+genstr + '\"'
    def randnumspacestr(self, length):
        import random
        genstr = ''.join([random.choice(StringGenerator.num) + " " for i in range(length//2)])
        return '\"'+genstr + '\"'
    def randsymstr(self, length):
        import random
        genstr = ''.join([random.choice(StringGenerator.sym) for i in range(length)])
        return '\"'+genstr + '\"'
    def randconvowstr(self, length):
        import random
        genstr = ''.join([random.choice(StringGenerator.con) + random.choice(StringGenerator.vow) for i in range(length//2)])
        return '\"'+genstr + '\"'

class Stringens:

    @staticmethod
    def letters():
        import random
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        while True:
            yield '\"'+ random.choice(alphabet) + '\"'


    @staticmethod
    def consonants():
        import random
        con = list("bcdfghjklmnpqrstvwxyz")
        while True:
            yield '\"'+ random.choice(con) + '\"'


    @staticmethod
    def vowels():
        import random
        vow = list("aeiou")
        while True:
            yield '\"'+ random.choice(vow) + '\"'

    #contiously generates a random literal string symbol
    @staticmethod
    def symbols():
        import random
        sym = list("~`!@#$%^&*()_+-=[]{}|;:<>?,.")
        while True:
            yield '\"'+ random.choice(sym) + '\"'