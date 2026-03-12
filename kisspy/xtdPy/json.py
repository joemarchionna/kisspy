import logging
import pathlib
import json
import os

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


def returnNone(*args, **kwargs):
    _logger.debug("No Data Provided, Returning None (Not Saving)")
    return None


def dumpData(filename: str, data: dict | list, onNoData=returnNone) -> str:
    """
    dumps the data to the filename specified, creating parent directories if neccessary

    Args:
        filename (str): filename, including path
        data (dict | list): the data to dump to JSON
        onNoData (callable, optional): a method expecting the filename and data as args, in that order. Defaults to returnNone

    Returns:
        str: filename
    """
    if not data:
        return onNoData(filename, data)
    pathlib.Path(os.path.split(filename)[0]).mkdir(parents=True, exist_ok=True)
    with open(filename, "w") as wtr:
        json.dump(data, wtr, indent=4)
    return filename


def returnDefault(*args, **kwargs) -> dict:
    """
    returns the JSON data\n
    expects the filename and data as args, in that order

    Returns:
        dict | list: JSON data
    """
    _logger.debug("'{}' Does Not Exist, Returning Default Data".format(args[0]))
    return args[1]


def createAndReturnDefault(*args, **kwargs) -> dict:
    """
    saves the JSON data to the path provided and returns the data\n
    expects the filename and data as args, in that order

    Returns:
        dict | list: JSON data
    """
    _logger.debug("'{}' Did Not Exist, Saved And Returning Default Data".format(args[0]))
    dumpData(args[0], args[1])
    return args[1]


def loadData(filename: str, defaultData=None, onNotExist=returnDefault) -> dict | list:
    """
    loads json data from the file specified

    Args:
        filename (str): filename
        defaultData (dict | list, optional): if the filename is not present, this value is passed to the onNotExist callable. Defaults to None
        onNotExist (callable, optional): a method expecting the filename and default data as args, in that order. Defaults to returnDefault

    Returns:
        dict | list: the JSON data in the file or defaultData
    """
    if not filename:
        _logger.debug("No Filename Provided, Returning Default Data")
        return defaultData
    if not os.path.exists(filename):
        if onNotExist:
            return onNotExist(filename, defaultData)
        return defaultData
    with open(filename) as rdr:
        return json.load(rdr)
