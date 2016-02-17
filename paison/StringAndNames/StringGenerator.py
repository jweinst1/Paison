#file that builds literal strings.



class StringGenerator:

    @staticmethod
    def letters():
        import random
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        while True:
            yield '\"'+ random.choice(alphabet) + '\"'

    @staticmethod
    def letters_string(length):
        import random
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        while True:
            letstr = ""
            for i in range(length):
                letstr += random.choice(alphabet)
            yield '\"' + letstr + '\"'
#yields a letter than a number string
    @staticmethod
    def alpha_num():
        import random
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        nums = list("0123456789")
        while True:
            yield '\"' + random.choice(alphabet) + random.choice(nums) + '\"'
  #yields a alphabet letter than a symbol
    @staticmethod
    def alpha_sym():
        import random
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        sym = list("~`!@#$%^&*()_+-=[]{}|;:<>?,.")
        while True:
            yield '\"' + random.choice(alphabet) + random.choice(sym) + '\"'

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
      #specified str of length, only symbols yielded
    @staticmethod
    def symbols_str(length):
        import random
        sym = list("~`!@#$%^&*()_+-=[]{}|;:<>?,.")
        while True:
            letstr = ""
            for i in range(length):
                letstr += random.choice(sym)
            yield '\"' + letstr + '\"'

    @staticmethod
    def numbers(maxn):
        import random
        while True:
            yield '\"'+ str(random.randrange(maxn)) + '\"'
      #continously yields con-vow-vow literal strings
    @staticmethod
    def conoostr():
        con = list("bcdfghjklmnpqrstvwxyz")
        vow = list("aouie")
        import random
        while True:
            chosen = random.choice(vow)
            yield '\"' + random.choice(con) + chosen + chosen + '\"'
    #generator that yields letters of the alphabet in sequence
    @staticmethod
    def linear_alpahbet():
        alphabet = list("abcdefghijklmnopqrstuvwxyz")