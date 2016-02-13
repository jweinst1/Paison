#file that contains different sets of string builders to produce instance methods on containers, like lists and tuples.


class ListMethodGenerator:

    @staticmethod
    def reverselist(self, name):
        return "{name}.reverse()".format(name=name)

    @staticmethod
    def sortlist(self, name):
        return "{name}.sort()".foramt(name=name)

    @staticmethod
    def poplist(self, name, number=""):
        return "{name}.pop({number})".format(name=name, number=number)

    @staticmethod
    def appendlist(self, name, elem):
        return "{name}.append({elem})",format(name=name, elem=elem)

    @staticmethod
    def extendlist(self, name, lst):
        return "{name}.extend({lst})".format(name=name, lst=lst)

    @staticmethod
    def countlist(self, name, elem):
        return "{name}.count({elem})".format(name=name, elem=elem)

    @staticmethod
    def removelist(self, name, elem):
        return "{name}.remove({elem})".format(name=name, elem=elem)