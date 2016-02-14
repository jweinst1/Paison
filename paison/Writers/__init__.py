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

    def varexpression(self, maxnum, length):
        import random
        expr = random.choice(self.variables)
        symbols = "+ - * / // % **".split(" ")
        for i in range(length):
            if i%2 is 0:
                expr += random.choice(symbols) + str(random.randrange(maxnum))
            else:
                expr += random.choice(symbols) + random.choice(self.variables)
        self.expressions.append(expr)

    def parenexpression(self, maxnum):
        import random
        symbols = "+ - * / // % **".split(" ")
        expr = random.choice(self.variables) + random.choice(symbols)
        expr += "(" + str(random.randrange(maxnum)) + random.choice(symbols) + str(random.randrange(maxnum)) + ")"
        self.expressions.append(expr)

     #creates a single mathematical expression as a mathematical method
    @staticmethod
    def singleexpression(self, variables, length, maxnum):
        import random
        expr = random.choice(variables)
        symbols = "+ - * / // % **".split(" ")
        for i in range(length):
            if i%2 is 0:
                expr += random.choice(symbols) + str(random.randrange(maxnum))
            else:
                expr += random.choice(symbols) + random.choice(variables)
        return expr

    #creates math expression in the form n symbol (m symbol c)
    @staticmethod
    def parenexpression(self, maxnum, variables):
        import random
        symbols = "+ - * / // % **".split(" ")
        expr = random.choice(variables) + random.choice(symbols)
        expr += "(" + str(random.randrange(maxnum)) + random.choice(symbols) + str(random.randrange(maxnum)) + ")"
        return expr