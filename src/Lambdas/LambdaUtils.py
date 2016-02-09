

class LambdaUtils:

    #converts lambda to function string
    @staticmethod
    def lambdatofunc(self, string):
        import re
        capture = re.match(r"^([a-z]+) \= lambda ([a-z]+)\: (.+)$")
        parts = capture.groups()
        return "def {name}({param}):\n  return {body}".format(name=parts[0], param=parts[1], body=parts[2])
