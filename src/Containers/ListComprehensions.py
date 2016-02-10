#file that contains the list comprehensions generator

class ListComprehensionGenerator:

    @staticmethod
    def rangecomp(self, end):
        return "[elem for elem in range({end})]".format(end=end)