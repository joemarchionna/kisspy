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
    if args:
        return args[0]
    return ""


def toNumeric(val, onFail=returnNone) -> float | int | None:
    """
    returns a float or int, by converting the provided val to a float and if possible, an int

    Args:
        val (_type_): the value to attempt to convert
        onFail (callable, optional): on error or failure, this is called with the value as the first arg / parameter and the exception as the second parameter. Defaults to returnNone

    Returns:
        float | int | None: resulting value
    """
    try:
        if isinstance(val, str):
            val = float(val)
        if int(val) == val:
            return int(val)
        return val
    except ValueError as verr:
        if not onFail:
            return None
        return onFail(val, verr)
