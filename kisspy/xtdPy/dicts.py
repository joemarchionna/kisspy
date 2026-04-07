import json


def getValueOfPath(data: dict, keyPath: str, defaultValue=None):
    """
    returns the value at the key path provided of a multi-level dict

    Args:
        data (dict): the dict to evaluate, ie: {'animals':{'dogs':{'whippet':'fast'}}}
        keyPath (str): key 'path' to work down using '/' as separators, ie: 'animals/dogs/whippet' returns 'fast'
        defaultValue (_type_, optional): default value returned if the path is not found. Defaults to None

    Returns:
        _type_: value of the final key of the path
    """
    mKeys = keyPath.split("/")
    dval = dict(data)
    for k in mKeys:
        dval = dval.get(k, None)
        if dval is None:
            dval = defaultValue
            break
    return dval


def setValueOfPath(data: dict, keyPath: str, value, createTree: bool = True) -> bool:
    """
    sets the value provided to the last key in the path

    Args:
        data (dict): the dict to evaluate
        keyPath (str): key 'path' to work down using '/' as separators
        value (_type_): value to set the last key of the path to
        createTree (bool, optional): if True, it creates a dict if any key in the path does not exist, otherwise does not set the value and exits. Defaults to True

    Returns:
        bool: True if the value was set, False if it did not set the value
    """
    if not keyPath:
        return False
    pKeys = keyPath.split("/")
    dval = data
    for i, k in enumerate(pKeys):
        if not isinstance(dval, dict):
            return False
        if (i + 1) < len(pKeys):
            if (k not in dval) and createTree:
                dval[k] = {}
            dval = dval.get(k, None)
        else:
            dval[k] = value
            return True
    return False


def deepCopy(data: dict | list) -> dict | list:
    """
    returns a true deep copy of the original data object by serializing to JSON and back again

    Args:
        data (dict|list): JSON-isable object

    Returns:
        dict|list: copy of the input data
    """
    jStr = json.dumps(data)
    return json.loads(jStr)


def addToDictIfExists(destination: dict, fieldName: str, fieldValue, normalizeTxtTo: str = None) -> bool:
    """
    adds the fieldvalue assigned to the fieldname key in the destination dictionary, if the fieldvalue is truthy

    Args:
        destination (dict): the dict to add the field to
        fieldName (str): the field or key name
        fieldValue (_type_): the field or key value
        normalizeTxtTo (str, optional): name of the method on the object to call to normalize, ie: 'lower'. Defaults to None

    Returns:
        bool: True if the value was set, False if it did not set the value
    """
    if not fieldValue:
        return False
    if isinstance(fieldValue, str) and normalizeTxtTo:
        mthd = getattr(fieldValue, normalizeTxtTo)
        if callable(mthd):
            fieldValue = mthd()
    destination[fieldName] = fieldValue
    return True
