import logging
import pathlib
import json
import os

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


def dumpData(filename: str, data) -> str:
    """
    dumps the data to the filename specified, creating parent directories if neccessary

    :param filename: filename, including path
    :type filename: str
    :param data: the data to dump to JSON
    :return: filename
    :rtype: str
    """
    if not filename:
        _logger.debug("No Filename Provided, Returning Filename")
        return filename
    pathlib.Path(os.path.split(filename)[0]).mkdir(parents=True, exist_ok=True)
    with open(filename, "w") as wtr:
        json.dump(data, wtr, indent=4)
    return filename


def loadData(filename: str, defaultData=None, createIfNotExist: bool = False) -> dict | list:
    """
    loads json data from the file specified

    :param filename: filename, including path
    :type filename: str
    :param defaultData: default data to return if the file does not exist
    :type defaultData: dict | list
    :param createIfNotExist: if filename does not exist, default data is provided, and this is set true, save the default data to the filename provided
    :type createIfNotExist: bool
    :return: loaded JSON content of the file
    :rtype: dict | list
    """
    if not filename:
        _logger.debug("No Filename Provided, Returning Default Data")
        return defaultData
    if not os.path.exists(filename):
        if defaultData and createIfNotExist:
            _logger.debug("Filename '{}' Did Not Exist, Saved And Returning Default Data".format(filename))
            dumpData(filename, defaultData)
            return defaultData
        _logger.debug("Filename '{}' Does Not Exist, Returning Default Data".format(filename))
        return defaultData
    with open(filename) as rdr:
        return json.load(rdr)
