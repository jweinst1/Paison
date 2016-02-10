#file that contains the main lambda generator
from src.StringAndNames.VariableGenerator import VarGenerator
from src.Containers.ListGenerator import ListGenerator
from src.Containers.ListComprehensions import ListComprehensionGenerator
class LambdaGenerator:
    mathsym = "+ - * / // % **".split(" ")

    def __init__(self):
        self.vargen = VarGenerator("syl")
        self.listgen = ListGenerator()
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
        select = random.randrange(1)
        if select is 0:
            body += "[elem for elem in range({arg})]".format(arg=param)
        self.writelambda(name, param, body)

    def printlambdas(self, type, amount):
        if type is "math":
            for i in range(amount):
                self.mathlambda(5, 10)
            result = "\n".join(self.bin)
            print(result)
            self.clear()
