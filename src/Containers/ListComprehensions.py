#file that contains the list comprehensions generator

#generates static templates for list comprhensions
class ListComprehensionGenerator:

    @staticmethod
    def rangecomp(self, end):
        return "[elem for elem in range({end})]".format(end=end)

    @staticmethod
    def rangecomp_t(self, end):
        return "(ele for ele in range({end}))".format(end=end)

    @staticmethod
    def repeatcomp(self, rep, end):
        return "[{rep} for elem in range({end})]".format(rep=rep, end=end)

    @staticmethod
    def repeatcomp_t(self, rep, end):
        return "({rep} for elem in range({end}))".format(rep=rep, end=end)

    @staticmethod
    def intervalcomp(self, start, end):
        return "[elem for elem in range({start}, {end})]".format(end=end, start=start)

    @staticmethod
    def intervalcomp_t(self, start, end):
        return "(elem for elem in range({start}, {end}))".format(end=end, start=start)