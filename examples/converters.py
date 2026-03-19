import sys

sys.path.append(".")

from kisspy import toNumeric, returnTxt, raiseValExc


def rtnMsg(*args):
    return "Can't Convert '{}' To A Number".format(args[0])


alphaVal = "55"
numVal = toNumeric(alphaVal)
print(isinstance(numVal, int))

alphaVal = "88 ft"
numVal = toNumeric(alphaVal)
print(numVal)

numVal = toNumeric(alphaVal, onFail=returnTxt)
print(numVal)

numVal = toNumeric(alphaVal, onFail=rtnMsg)
print(numVal)

numVal = toNumeric(alphaVal, onFail=raiseValExc)
