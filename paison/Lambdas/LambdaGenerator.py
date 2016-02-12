#file that contains the main lambda generator
from paison.StringAndNames.VariableGenerator import VarGenerator
from paison.Containers.ListGenerator import ListGenerator
from paison.Containers.ListComprehensions import ListComprehensionGenerator
class LambdaGenerator:
    mathsym = "+ - * / // % **".split(" ")

    def __init__(self):
        self.vargen = VarGenerator("syl")
        self.listgen = ListGenerator()
        self.liscomp = ListComprehensionGenerator
        self.bin = []
    def __repr__(self):
        return str(self.bin)
    def writelambda(self, name, param, body):
        lstring = "{name} = lambda {param}: {body}".format(name=name, param=param, body=body)
        self.bin.append(lstring)
    def clear(self):
        self.bin = []

    #writes a random lambda expression
    def mathlambda(self, length, maxnum):
        import random
        name = self.vargen.genvar(6)
        param = random.choice(self.vargen.alphabet)
        body = ""
        body += param
        for i in range(length):
            body += random.choice(LambdaGenerator.mathsym) + str(random.randrange(maxnum))
        self.writelambda(name, param, body)

    def makelistlambda(self, length):
        import random
        name = self.vargen.genvar(6)
        param = random.choice(self.vargen.alphabet)
        body = ""
        select = random.randrange(5)
        if select is 0:
            body += self.liscomp.rangecomp(param)
        elif select is 1:
            body += self.liscomp.rangecomp_t(param)
        elif select is 2:
            body += self.liscomp.repeatcomp(str(select), param)
        elif select is 3:
            body += self.liscomp.repeatcomp(param, param)
        elif select is 4:
            body += self.liscomp.repeatcomp_t(param, param)
        elif select is 5:
            body += self.liscomp.evencomp(param)
        elif select is 6:
            body += self.liscomp.oddcomp(param)
        self.writelambda(name, param, body)

    def printlambdas(self, type, amount):
        if type is "math":
            for i in range(amount):
                self.mathlambda(5, 10)
            result = "\n".join(self.bin)
            print(result)
            self.clear()
    def createlambdas(self, type, amount):
        if type is "math":
            for i in range(amount):
                self.mathlambda(5, 10)
            result = "\n".join(self.bin)
            self.clear()
            return result
    #used to create a specified amount of a random type of lambdas
    def createrandlambdas(self, amount):
        pass
