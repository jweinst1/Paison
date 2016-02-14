#file that contains class that produces index expressions.

class IndexExpressionGenerator:

    @staticmethod
    def getitemzero(name):
        return "{name}[0]".format(name=name)

    @staticmethod
    def getitemcustom(name, number):
        assert number.__class__ is int
        return "{name}[{number}]".format(name=name, number=number)

    @staticmethod
    def getitemslice(name, start, end):
        return "{name}[{start}:{end}]".format(name=name, start=start, end=end)

    @staticmethod
    def getitemreverse(name):
        return "{name}[::-1]".format(name=name)

    @staticmethod
    def addfirsttwoindex(name):
        return "{name}[0] + {name}[1]".format(name=name)

    @staticmethod
    def addsecondtofirstindex(name):
        return "{name}[0] += {name}[1]".format(name=name)

    @staticmethod
    def subtractfirsttwoindex(name):
        return "{name}[0] - {name}[1]".format(name=name)

    @staticmethod
    def subtractsecondfromfirstindex(name):
        return "{name}[0] -= {name}[1]".format(name=name)

    @staticmethod
    def setfirsttosecond(name):
        return "{name}[0] = {name}[1]".format(name=name)

    @staticmethod
    def setfirstsquared(name):
        return "{name}[0] = {name}[0]**{name}[0]".format(name=name)

    @staticmethod
    def nullifyfirst(name):
        return "{name}[0] = None".format(name=name)

    @staticmethod
    def nullifycustom(name, number):
        return "{name}[{number}] = None".format(number=number, name=name)