import datetime

SORTABLE_DT_FRMT = "%Y%m%d.%H%M%S"
SORTABLE_DT_TZA_FRMT = "%Y%m%d.%H%M%S%z"
PYLOG_DT_FRMT = "%Y-%m-%d %H:%M:%S,%f"


def getSortableNow(prefix=None, suffix=None, frmt: str = SORTABLE_DT_FRMT):
    """
    returns the date and time as a sortable string separated by a period ie: 'YYYYmmdd.HHMMSS' or the format provided;\n
    prefix: str added before sortable date/time;\n
    suffix: str added after sortable date/time;\n
    frmt: str, format to output datetime as
    """
    val = ""
    if prefix:
        val = prefix
    val = val + datetime.datetime.now().strftime(frmt)
    if suffix:
        val = val + suffix
    return val
