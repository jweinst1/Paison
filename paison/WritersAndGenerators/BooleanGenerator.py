
#generators that yield random boolean expressions
class BooleanGenerators:

    @staticmethod
    def boolean_is_number(x, y):
        import random
        while True:
            yield "{x} is {y}".format(x=random.randrange(x), y=random.randrange(y))

    @staticmethod
    def boolean_ne_number(x, y):
        import random
        while True:
            yield "{x} != {y}".format(x=random.randrange(x), y=random.randrange(y))

    @staticmethod
    def boolean_gt_number(x, y):
        import random
        while True:
            yield "{x} > {y}".format(x=random.randrange(x), y=random.randrange(y))

    @staticmethod
    def boolean_lt_number(x, y):
        import random
        while True:
            yield "{x} < {y}".format(x=random.randrange(x), y=random.randrange(y))
#random literal letter comparison
    @staticmethod
    def boolean_is_letter():
        import random
        letters = list("abcdefghijklmnopqrstuvwxyz")
        while True:
            x = "\"" + random.choice(letters) + "\""
            y = "\"" + random.choice(letters) + "\""
            yield "{x} is {y}".format(x=x, y=y)