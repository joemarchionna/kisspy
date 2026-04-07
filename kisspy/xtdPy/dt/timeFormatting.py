import datetime

SORTABLE_DT_FRMT = "%Y%m%d.%H%M%S"
SORTABLE_DT_TZA_FRMT = "%Y%m%d.%H%M%S%z"
PYLOG_DT_FRMT = "%Y-%m-%d %H:%M:%S,%f"


def getSortableNow(prefix: str = None, suffix: str = None, frmt: str = SORTABLE_DT_FRMT) -> str:
    """
    returns the date and time as a sortable string separated by a period ie: 'YYYYmmdd.HHMMSS' or the format provided

    Args:
        prefix (str, optional): text added before sortable date/time. Defaults to None
        suffix (str, optional): text added before sortable date/time. Defaults to None
        frmt (str, optional): datatime output format. Defaults to SORTABLE_DT_FRMT

    Returns:
        str: the current datetime formatted as specified
    """
    val = ""
    if prefix:
        val = prefix
    val = val + datetime.datetime.now().strftime(frmt)
    if suffix:
        val = val + suffix
    return val
