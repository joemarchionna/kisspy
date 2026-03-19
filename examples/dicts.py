import sys

sys.path.append(".")

from kisspy import setValueOfPath, getValueOfPath

vd = {"animals": {"dog": {"whippet": "fast", "lab": "slower"}}}

wv = getValueOfPath(vd, keyPath="animals/dog/lab")
print(wv)

cv = getValueOfPath(vd, keyPath="animals/cat/tabby")
print(cv)

setValueOfPath(vd, "animals/dog/golden", "silly")
print(vd)
