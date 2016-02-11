#file that contains class that produces index expressions.

class IndexExpressionGenerator:

    @staticmethod
    def getitemzero(self, name):
        return "{name}[0]".format(name=name)