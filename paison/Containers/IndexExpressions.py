#file that contains class that produces index expressions.

class IndexExpressionGenerator:

    @staticmethod
    def getitemzero(self, name):
        return "{name}[0]".format(name=name)

    @staticmethod
    def getitemcustom(self, name, number):
        assert number.__class__ is int
        return "{name}[{number}]".format(name=name, number=number)

    @staticmethod
    def getitemslice(self, name, start, end):
        return "{name}[{start}:{end}]".format(name=name, start=start, end=end)

    @staticmethod
    def getitemreverse(self, name):
        return "{name}[::-1]".format(name=name)

    @staticmethod
    def addfirsttwoindex(self, name):
        return "{name}[0] + {name}[1]".format(name=name)

    @staticmethod
    def addsecondtofirstindex(self, name):
        return "{name}[0] += {name}[1]".format(name=name)

    @staticmethod
    def subtractfirsttwoindex(self, name):
        return "{name}[0] - {name}[1]".format(name=name)

    @staticmethod
    def subtractsecondfromfirstindex(self, name):
        return "{name}[0] -= {name}[1]".format(name=name)

    @staticmethod
    def setfirsttosecond(self, name):
        return "{name}[0] = {name}[1]".format(name=name)

    @staticmethod
    def setfirstsquared(self, name):
        return "{name}[0] = {name}[0]**{name}[0]".format(name=name)

    @staticmethod
    def nullifyfirst(self, name):
        return "{name}[0] = None".format(name=name)

    @staticmethod
    def nullifycustom(self, name, number):
        return "{name}[{number}] = None".format(number=number, name=name)