import threading


def thrdSafeSync(func):
    """
    decorator that makes the function thread safe

    Args:
        func (_type_): the method to decorate

    Example:

        ````python
        @thrdSafeSync
        def oneAtATime():
            file IO process...
        ````
    """
    lock = threading.Lock()  # A lock for this specific function

    def wrapper(*args, **kwargs):
        with lock:  # Acquire and release the lock using 'with' statement
            return func(*args, **kwargs)

    return wrapper
