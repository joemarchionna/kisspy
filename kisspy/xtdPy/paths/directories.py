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
    d, f = os.path.split(filename)
    d = frmtPath(d, convertToFwdSlsh, endInSeparator)
    return d, f


def createDir(fqFilename: str, directory: str = None, convertToFwdSlsh: bool = True, endInSeparator: bool = True) -> str:
    """
    creates the parent directories if they do not exist;\n
    takes either filename (including directories) or directory parameter\n
    returns the directory
    """
    if fqFilename:
        directory, f = splitPath(fqFilename, convertToFwdSlsh, endInSeparator)
    else:
        directory = frmtPath(directory, convertToFwdSlsh, endInSeparator)
    _createDir(directory)
    return directory


def expandUser(path: str, expandChar: str = "~", convertToFwdSlsh: bool = True, endInSeparator: bool = False) -> str:
    """
    expands the path to a fully qualified path using the expandChar as a signal to do so\n
    replaces back slashes to forward slashes if convertToFwdSlsh is true\n
    returns the path as a simple string
    """
    if not path or not path.startswith(expandChar):
        return path
    homeDir = frmtPath(str(pathlib.Path.home()), convertToFwdSlsh, endInSeparator)
    return path.replace(expandChar, homeDir)
