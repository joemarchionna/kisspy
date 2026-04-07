from functools import reduce
import string

# https://stackoverflow.com/questions/48983939/convert-a-number-to-excel-s-base-26
# this works for SBS plates as well


def _divmod_excel(n):
    a, b = divmod(n, 26)
    if b == 0:
        return a - 1, b + 26
    return a, b


def toExcelCol(columnNum: int) -> str:
    """
    converts a 1-based column number to Excel-ish column name, ie: 1 -> A; 27 -> AA

    Args:
        columnNum (int): the column number

    Returns:
        str: the column name
    """
    chars = []
    while columnNum > 0:
        columnNum, d = _divmod_excel(columnNum)
        chars.append(string.ascii_uppercase[d - 1])
    return "".join(reversed(chars))


def fromExcelCol(columnName: str) -> int:
    """
    converts an Excel column name to a 1-based integer, ie: A -> 1; AA -> 27

    Args:
        columnName (str): the column name

    Returns:
        int: the column number
    """
    return reduce(lambda r, x: r * 26 + x + 1, map(string.ascii_uppercase.index, columnName), 0)
