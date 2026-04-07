from kisspy.xtdPy.paths.directories import expandUser
from kisspy.xtdPy.json import loadData
from typing import Tuple
import datetime
import pathlib
import logging
import os

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


def lastModifiedDT(fqFilename: str) -> datetime.datetime:
    """
    returns a datetime object for the last modified datetime of the file specified

    Args:
        fqFilename (str): the path to the file

    Returns:
        datetime.datetime: last modified datetime
    """
    try:
        pth = pathlib.Path(fqFilename)
        return datetime.datetime.fromtimestamp(pth.stat().st_mtime)
    except:
        return None


def _getFn(directory: str, fn: str) -> str:
    """returns a string as the filepath"""
    return "{}/{}".format(expandUser(directory), fn)


def searchForFile(filename: str, directories: list[str]) -> str:
    """
    searches for a file in the locations provided and returns the file path;\n
    will expand to the user's home folder if a path starts with ~

    Args:
        filename (str): the file name to search for
        directories (list[str]): a list of possible locations, ie directories

    Returns:
        str: the file path to the existing (found) file
    """
    for fn in [_getFn(x, filename) for x in directories]:
        _logger.debug("Searching For File '{}'".format(fn))
        if os.path.exists(fn) and os.path.isfile(fn):
            return fn
    return None


def searchAndload(filename: str, directories: list[str], defaultData: dict | list = None) -> Tuple[str, dict]:
    """
    searches for a file in the locations provided; if a file is found, it \n
    loads the file with json and returns the file's content;\n
    will expand to the user's home folder if a path starts with ~

    Args:
        filename (str): the file name to search for
        directories (list[str]): a list of possible locations, ie directories
        defaultData (dict|list, optional): default data to return if no file is present. Defaults to None

    Returns:
        Tuple[str, dict]: a tuple: found file name and file content
    """
    fn = searchForFile(filename, directories)
    if fn:
        _logger.debug("Found File '{}'".format(fn))
        return fn, loadData(fn, defaultData)
    return None, defaultData
