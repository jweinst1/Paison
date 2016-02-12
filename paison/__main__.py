#main commandline file for package
from paison.Lambdas.LambdaGenerator import LambdaGenerator
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

lambdamach = LambdaGenerator()
newfile = open(sys.argv[1], "w")
newstr = lambdamach.createlambdas("math", 100)
newfile.write(newstr)
newfile.close()
print("done")



