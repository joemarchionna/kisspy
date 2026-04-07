from kisspy.xtdPy.paths._common import frmtPath
from typing import Tuple
import pathlib
import os


def _createDir(directory: str) -> bool:
    if os.path.exists(directory):
        return False
    pathlib.Path(directory).mkdir(parents=True, exist_ok=True)
    return True


def splitPath(filename: str, convertToFwdSlsh: bool = True, endInSeparator: bool = True) -> Tuple[str, str]:
    """
    splits the filename to the path and basename - same as os.path.split except converts to forward slashes and endings if specified

    Args:
        filename (str): path to split
        convertToFwdSlsh (bool, optional): converts any backslash to forward slash if True. Defaults to True
        endInSeparator (bool, optional): ends the directory path with a slash if specified. Defaults to True

    Returns:
        Tuple[str, str]: directory path, basename
    """
    d, f = os.path.split(filename)
    d = frmtPath(d, convertToFwdSlsh, endInSeparator)
    return d, f


def createDir(fqFilename: str, directory: str = None, convertToFwdSlsh: bool = True, endInSeparator: bool = True) -> str:
    """
    creates the parent directories if they do not exist

    Args:
        fqFilename (str): fully-qualified filename with path - set to None if providing just a directory parameter
        directory (str, optional): directory to create. Defaults to None
        convertToFwdSlsh (bool, optional): converts any backslash to forward slash if True. Defaults to True
        endInSeparator (bool, optional): ends the directory path with a slash if specified. Defaults to True

    Returns:
        str: directory
    """
    if fqFilename:
        directory, f = splitPath(fqFilename, convertToFwdSlsh, endInSeparator)
    else:
        directory = frmtPath(directory, convertToFwdSlsh, endInSeparator)
    _createDir(directory)
    return directory


def expandUser(path: str, expandChar: str = "~", convertToFwdSlsh: bool = True, endInSeparator: bool = False) -> str:
    """
    expands the path to a fully qualified path using the expandChar as a signal to do so

    Args:
        path (str): _description_
        expandChar (str, optional): representative char for the user directory. Defaults to "~"
        convertToFwdSlsh (bool, optional): converts any backslash to forward slash if True. Defaults to True
        endInSeparator (bool, optional): ends the directory path with a slash if specified. Defaults to False

    Returns:
        str: path
    """
    if not path or not path.startswith(expandChar):
        return path
    homeDir = frmtPath(str(pathlib.Path.home()), convertToFwdSlsh, endInSeparator)
    return path.replace(expandChar, homeDir)
