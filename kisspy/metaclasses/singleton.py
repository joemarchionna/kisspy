class Singleton(type):
    """
    meta-class to create a single instance of a class

    Example:
        ````python
        class MyClass(<baseClass>, metaclass=Singleton):\n
            pass
        ````
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
