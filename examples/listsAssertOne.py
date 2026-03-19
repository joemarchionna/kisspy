import sys

sys.path.append(".")

from kisspy import assertOne
from kisspy.exceptions import TooManyRecordsException, ZeroRecordsException


def thrwZeroRecordsEx(*args, **kwargs):
    raise ZeroRecordsException()


vl = [2, 4, 6, 8]
print(assertOne([]))
print(assertOne([44]))

try:
    oneValue = assertOne(vl)
except TooManyRecordsException as err:
    print(err.toStrWithTyp())

try:
    print(assertOne([], onZeroRcds=thrwZeroRecordsEx))
except ZeroRecordsException as err:
    print(err.toStrWithTyp())
