from kisspy.exceptions import TooManyRecordsException

NO_VALUE = "__no_value__"


def binRecordsOnKey(elements: list[dict], key: str, noKeyOrValue: str = NO_VALUE) -> list[list[dict]]:
    """
    returns a list within a list where the internal lists are binned
    based on the values of the key in the original list

    Args:
        elements (list[dict]): original list of objects
        key (str): key to evaluate value of when binning objects
        noKeyOrValue (str, optional): if set will bin records with missing or null values together. to not bin missing or null values set to 'None'. Defaults to NO_VALUE

    Returns:
        list[list[dict]]: binned records based on value

    Example:
    ````python
        i = [{'a':1}, {'a':2}, {'a':2}, {'a':1}, {'a':4}, {'a':1}, {'a':5} ]
        z = binRecordsOnKey(i, 'a')
        z = [
                [{'a':1}, {'a':1}, {'a':1}],
                [{'a':2}, {'a':2}],
                [{'a':4}],
                [{'a':5}]
            ]
    ````
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
    appends the object provided to the list provided IF the object is not in the list already

    Args:
        lst (list): the list to possibly append the value to
        obj (_type_): the object to append to the list

    Returns:
        bool: True if the object was appended to the list, otherwise False
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
    NOTE: the callables are passed the records list as an arg

    Args:
        records (list): the list to be evaluated
        onZeroRcds (callable, optional): if the list is empty or None, returns the result of the callable if provided. Defaults to None
        onMultiRcds (callable, optional): if the length of the list is greater than one, returns the result of the callable if provided. Defaults to raising a TooManyRecordsException

    Returns:
        dict | list: single record object or None
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
