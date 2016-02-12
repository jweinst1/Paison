#file that contains different sets of string builders to produce instance methods on containers, like lists and tuples.


class ListMethodGenerator:

    @staticmethod
    def reverselist(self, name):
        return "{name}.reverse()".format(name=name)

    @staticmethod
    def sortlist(self, name):
        return "{name}.sort()".foramt(name=name)

    @staticmethod
    def poplist(self, name, number=None):
        pass