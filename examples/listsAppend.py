import sys

sys.path.append(".")

from kisspy import appendUnique

vl = [2, 4, 6, 8]
if appendUnique(vl, 4):
    print("Added 4 Again: {}".format(vl))

if appendUnique(vl, 10):
    print("Added 10: {}".format(vl))
