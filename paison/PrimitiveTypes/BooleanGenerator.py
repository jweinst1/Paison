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
    def boolean_ge_number(x, y):
        import random
        while True:
            yield "{x} >= {y}".format(x=random.randrange(x), y=random.randrange(y))

    @staticmethod
    def boolean_lt_number(x, y):
        import random
        while True:
            yield "{x} < {y}".format(x=random.randrange(x), y=random.randrange(y))

    @staticmethod
    def boolean_le_number(x, y):
        import random
        while True:
            yield "{x} <= {y}".format(x=random.randrange(x), y=random.randrange(y))
#random literal letter comparison
    @staticmethod
    def boolean_is_letter():
        import random
        letters = list("abcdefghijklmnopqrstuvwxyz")
        while True:
            x = "\"" + random.choice(letters) + "\""
            y = "\"" + random.choice(letters) + "\""
            yield "{x} is {y}".format(x=x, y=y)

    @staticmethod
    def boolean_not_num(n):
        import random
        while True:
            yield "not {num}".format(num=random.randrange(n))

     ##VARIABLE BOOLAN GENERATORS
    @staticmethod
    def var_is_num(varname):
        import random
        while True:
            yield "{x} is {y}".format(x=varname, y=random.randrange(20))

    @staticmethod
    def var_eq_num(varname):
        import random
        while True:
            yield "{x} == {y}".format(x=varname, y=random.randrange(20))


    @staticmethod
    def var_lt_num(varname):
        import random
        while True:
            yield "{x} < {y}".format(x=varname, y=random.randrange(20))


    @staticmethod
    def var_gt_num(varname):
        import random
        while True:
            yield "{x} > {y}".format(x=varname, y=random.randrange(20))

    @staticmethod
    def var_le_num(varname):
        import random
        while True:
            yield "{x} <= {y}".format(x=varname, y=random.randrange(20))


    @staticmethod
    def var_ge_num(varname):
        import random
        while True:
            yield "{x} >= {y}".format(x=varname, y=random.randrange(20))


    @staticmethod
    def var_ne_num(varname):
        import random
        while True:
            yield "{x} != {y}".format(x=varname, y=random.randrange(20))


#handles chains of or or and statements
class ChainBooleanGenerator:

    @staticmethod
    def var_and_is_num(length, varname):
        import random
        while True:
            tempstr = "{x} is {y}".format(x=varname, y=random.randrange(20))
            for i in range(length-1):
                tempstr += " and " + "{x} is {y}".format(x=varname, y=random.randrange(20))
            yield tempstr

    @staticmethod
    def var_or_is_num(length, varname):
        import random
        while True:
            tempstr = "{x} is {y}".format(x=varname, y=random.randrange(20))
            for i in range(length-1):
                tempstr += " or " + "{x} is {y}".format(x=varname, y=random.randrange(20))
            yield tempstr

