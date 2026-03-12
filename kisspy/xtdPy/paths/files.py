from kisspy.xtdPy.paths.directories import expandUser
from kisspy.xtdPy.json import loadData
from typing import Tuple
import datetime
import pathlib
import logging
import os

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


def lastModifiedDT(fqFilename) -> datetime.datetime:
    """returns a datetime object for the file specified, or None if it fails"""
    try:
        pth = pathlib.Path(fqFilename)
        return datetime.datetime.fromtimestamp(pth.stat().st_mtime)
    except:
        return None


def _getFn(directory: str, fn: str) -> str:
    """returns a string as the filepath"""
    return "{}/{}".format(expandUser(directory), fn)


def searchForFile(filename: str, locations: list[str]) -> str:
    """
    searches for a file in the locations provided and returns the fn\n
    locations can include the home directory designation '~'
    """
    for fn in [_getFn(x, filename) for x in locations]:
        _logger.debug("Searching For File '{}'".format(fn))
        if os.path.exists(fn) and os.path.isfile(fn):
            return fn
    return None


def searchAndload(filename: str, directories: list[str], defaultData=None) -> Tuple[str, dict]:
    """
    searches for a file in the format location/appName/filename and returns the fn and loaded json content\n
    directories can include the home directory designation '~'
    """
    fn = searchForFile(filename, directories)
    if fn:
        _logger.debug("Found File '{}'".format(fn))
        return fn, loadData(fn, defaultData)
    return None, defaultData
