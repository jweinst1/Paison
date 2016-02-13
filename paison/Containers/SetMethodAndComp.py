#file for dealing with set methods and comprehensions

#generates set method strings
class SetMethodsGenerator:

    @staticmethod
    def setadd(self, name, elem):
        return "{name}.add({elem})".format(name=name, elem=elem)

    @staticmethod
    def setremove(self, name, elem):
        return "{name}.remove({elem})".format(name=name, elem=elem)

    @staticmethod
    def popset(self, name, elem=""):
        return "{name}.pop({elem})".format(name=name, elem=elem)

    @staticmethod
    def copy(self, name):
        return "{name}.copy()".format(name=name)