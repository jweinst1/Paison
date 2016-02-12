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

    @staticmethod
    def mathcomp(self, expr, end):
        return "[elem{expr} for elem in range({end})]".format(end=end, expr=expr)

    @staticmethod
    def evencomp(self, end):
        return "[elem for elem in range({end}) if elem%2==0]".format(end=end)

    @staticmethod
    def evecomp_t(self, end):
        return "(elem for elem in range({end}) if elem%2==0)".format(end=end)

    @staticmethod
    def oddcomp(self, end):
        return "[elem for elem in range({end}) if elem%2!=0]".format(end=end)

    @staticmethod
    def oddcomp_t(self, end):
        return "(elem for elem in range({end}) if elem%2!=0)".format(end=end)