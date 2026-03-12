from kisspy.exceptions import PidFilePresentException
from functools import wraps
import os

PID_FN = "wkdir/appPID.txt"


def pidFile(filename: str = PID_FN):
    """
    will allow method decorated to run only if the pid file specified is not present\n
    if filename is set to None this will have no effect (will allow multiple instances)
    """

    def pidFileDecorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if filename:
                    if os.path.exists(filename):
                        raise PidFilePresentException("Method Already Running!")
                    with open(filename, "w") as wtr:
                        wtr.write("{}\n".format(os.getpid()))
                results = func(*args, **kwargs)
                if filename:
                    os.remove(filename)
                return results
            except PidFilePresentException as pidErr:
                print("{}: {}".format(PidFilePresentException.__name__, pidErr))

        return wrapper

    return pidFileDecorator
