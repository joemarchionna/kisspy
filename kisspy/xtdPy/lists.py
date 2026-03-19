from kisspy.exceptions import TooManyRecordsException

NO_VALUE = "__no_value__"


def binRecordsOnKey(elements: list[dict], key: str, noKeyOrValue: str = NO_VALUE) -> list[list[dict]]:
    """
    returns a list within a list where the internal lists are binned based on the values of the key in the original list\n
    will bin missing or null values together; to not bin null or missing key records, set noKeyOrValue = None\n
    ie:\n
    i = [{'a':1},{'a':2},{'a':2},{'a':1},{'a':4},{'a':1},{'a':5}]\n
    z = binRecordsOnKey(i, 'a')\n
    z is [ \n
        [{'a':1},{'a':1},{'a':1}], \n
        [{'a':2},{'a':2}], \n
        [{'a':4}], \n
        [{'a':5}] \n
    ]
    """
    uniqueKeyValues = []
    for e in elements:
        kv = e.get(key, noKeyOrValue)
        if kv and (kv not in uniqueKeyValues):
            uniqueKeyValues.append(kv)
    dividedLists = []
    for ukv in uniqueKeyValues:
        dividedLists.append([x for x in elements if x.get(key, noKeyOrValue) == ukv])
    return dividedLists


def appendUnique(lst: list, obj) -> bool:
    """
    appends the object provided to the list provided IF the object is not in the list already\n
    lst: list, the list to append the value to\n
    obj: object, the object to append to the list\n
    returns True if the object was appended to the list, otherwise False
    """
    if obj in lst:
        return False
    lst.append(obj)
    return True


def thrwMultiRcdExc(*args, **kwargs):
    raise TooManyRecordsException(numberRecords=len(args[0]))


def assertOne(records: list, onZeroRcds=None, onMultiRcds=thrwMultiRcdExc) -> dict | list:
    """
    if the list has only one record, returns the only record\n
    if the list is empty or None, returns the result of the\n
     onZeroRcds callable if provided else None\n
    if the length of the list is greater than one, returns the\n
     result of the onMultiRcds callable if provided else the original\n
     list; default action is raise an TooManyRecordsException\n
    the callables are passed the records list as an arg
    """
    if not records:
        if onZeroRcds:
            return onZeroRcds(records)
        return None
    if len(records) > 1:
        if onMultiRcds:
            return onMultiRcds(records)
        return records
    return records[0]


# def _cleanValue(value, caseSensitive=False):
#     if not isinstance(value, str):
#         return None
#     value = value.strip()
#     if not caseSensitive:
#         value = value.lower()
#     return value


# def getExactMatches(
#     records: list[dict], keyName: str, compareTo: str, caseSensitive=False, onCleanValue=_cleanValue
# ) -> list[dict]:
#     """
#     returns a list of records where the keyName's value matches the compareTo value\n
#     recordList: list, the list to evaluate\n
#     keyName: str, the dict key of each record to compare compareTo to\n
#     compareTo: str, the value to compare to\n
#     caseSensitive: bool, if False (default), comparison is done case-insensitive and vice-versa\n
#     onCleanValue: callable, method to call to clean the value
#     """
#     exactMatches = []
#     compareTo = onCleanValue(compareTo, caseSensitive)
#     for r in records:
#         v = onCleanValue(r.get(keyName, None), caseSensitive)
#         if v and (v == compareTo):
#             exactMatches.append(r)
#     return exactMatches
