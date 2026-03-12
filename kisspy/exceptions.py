class KisspyException(Exception):
    pass


class PidFilePresentException(KisspyException):
    pass


class TooManyRecordsException(KisspyException):
    MSG_FORMAT = "{} {} Returned, {} Were Expected"

    def __init__(self, *args: object, numberRecords: int = None, recordType: str = "Records", numberExpected: int = 1) -> None:
        if numberRecords and recordType:
            msg = TooManyRecordsException.MSG_FORMAT.format(numberRecords, recordType, numberExpected)
            super().__init__(msg, *args)
        else:
            super().__init__(*args)
