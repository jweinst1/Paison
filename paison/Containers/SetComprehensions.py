#file for dealing with set methods and comprehensions

class SetComprehensionGenerator:

    @staticmethod
    def addset(self, name, elem):
        return "{name}.add({elem})".format(name=name, elem=elem)