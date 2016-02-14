#package for dealing with string writers

class Writer:

    def __init__(self, variables):
        self.variables = variables
        self.expressions = []
    def __repr__(self):
        return str(self.expressions)
    def clear(self):
        self.expressions = []
    def getlines(self):
        return '\n'.join(self.expressions)
    def getoneline(self):
        return ','.join(self.expressions)

class MathWriter(Writer):
    #writes empty math expr
    def emptyexpression(self, maxnum, length):
        import random
        symbols = "+ - * / // % **".split(" ")
        expr = str(random.randrange(maxnum))
        for i in range(length):
            expr += random.choice(symbols) + str(random.randrange(maxnum))
        self.expressions.append(expr)
        