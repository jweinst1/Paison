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