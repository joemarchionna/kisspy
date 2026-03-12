import json


def getValueOfPath(data: dict, keyPath: str, defaultValue=None):
    """
    returns the value at the key path provided;\n
    data: dict, the dictionary to evaluate, ie: {'animals':{'dogs':{'whippet':'fast'}}};\n
    keyPath: str, key 'tree' to work down using '/' as separators, ie: 'animals/dogs/whippet' returns 'fast';\n
    defaultValue: any, default value returned if the path is not found
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
    sets the value provided to the last key in the path\n
    returns true if the value was able to be set, false if any of the tree was not a dict and therefore unable to be set\n
    if createTree is true, it creates a dict if any key in the path does not exist, otherwise does not set the value and exits
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


def deepCopy(data):
    """
    returns a true deep copy of the original data object by serializing to JSON and back again
    """
    jStr = json.dumps(data)
    return json.loads(jStr)


def addToDictIfExists(destination: dict, fieldName: str, fieldValue, normalizeTxtTo: str = None):
    """
    adds the fieldvalue assigned to the fieldname key in the destination dictionary, if the fieldvalue is not 'None'\n
    if normalizeTxtTo is a callable function, it will call that function when setting, ie: 'lower'
    """
    if fieldValue:
        if isinstance(fieldValue, str) and normalizeTxtTo:
            mthd = getattr(fieldValue, normalizeTxtTo)
            if callable(mthd):
                fieldValue = mthd()
        destination[fieldName] = fieldValue
    return destination
