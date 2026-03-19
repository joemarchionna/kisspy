def raiseValExc(*args, **kwargs):
    """raises a ValueError with the first argument displayed in single quotes as part of the error message"""
    msg = "The Value '{}' Could Not Be Converted To A Numeric Value".format(args[0])
    args[1].add_note(msg)
    raise args[1]


def returnNone(*args, **kwargs) -> None:
    """returns Python None variable regardless of arguments passed"""
    return None


def returnTxt(*args, **kwargs) -> None:
    """returns the first argument, does nothing else"""
    return args[0]


def toNumeric(val, onFail=returnNone) -> float | int | None:
    """
    returns a float or int, by converting the provided val\n
    \t to a float and if possible, an int\n
    on error, it calls onFail providing val as the first parameter\n
    \t by default, returns None
    """
    try:
        if isinstance(val, str):
            val = float(val)
        if int(val) == val:
            return int(val)
        return val
    except ValueError as verr:
        return onFail(val, verr)
