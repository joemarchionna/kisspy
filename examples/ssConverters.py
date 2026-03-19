import sys

sys.path.append(".")

from kisspy.converters.excelHelpers import fromExcelCol, toExcelCol

col = "C"
print(fromExcelCol(col))

col = "AF"
print(fromExcelCol(col))

num = 2
print(toExcelCol(num))

num = 33
print(toExcelCol(num))
