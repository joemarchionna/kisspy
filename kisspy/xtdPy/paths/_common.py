def addEndingSeparator(path: str, sep: str = "/") -> str:
    """ensure the path ends in the separator specified"""
    if path.endswith(sep):
        return path
    return path + sep


def removeEndingSeparator(path: str, sep: str = "/") -> str:
    """ensure the path does not end in the separator specified"""
    if not path.endswith(sep):
        return path
    return path[: (len(path) - 1)]


def frmtPath(path: str, convertToFwdSlsh: bool, endInSeparator: bool) -> str:
    if convertToFwdSlsh:
        path = path.replace("\\", "/")
    if endInSeparator:
        path = addEndingSeparator(path)
    return path
