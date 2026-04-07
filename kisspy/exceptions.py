class KisspyException(Exception):
    def toStrWithTyp(self) -> str:
        return "{}: {}".format(type(self).__name__, self)


class PidFilePresentException(KisspyException):
    pass


class TooManyRecordsException(KisspyException):
    MSG_FORMAT = "{} {} Returned, {} Were Expected"

    def __init__(self, *args: object, numberRecords: int = None, recordType: str = "Records", numberExpected: int = 1) -> None:
        self.numberRecords = numberRecords
        self.numberExpected = numberExpected
        self.recordType = recordType
        if numberRecords and recordType:
            msg = TooManyRecordsException.MSG_FORMAT.format(numberRecords, recordType, numberExpected)
            super().__init__(msg, *args)
        else:
            super().__init__(*args)


class ZeroRecordsException(KisspyException):
    MSG_FORMAT = "Zero (0) {} Returned, > 0 Were Expected"

    def __init__(self, *args, recordType: str = "Records"):
        self.recordType = recordType
        if args:
            super().__init__(*args)
        else:
            msg = ZeroRecordsException.MSG_FORMAT.format(recordType)
            super().__init__(msg, *args)
