def singleton(_class):
    """
    class decorator to create a single instance of a class

    Args:
        _class (_type_): the class to decorate

    Example:
        ````python
        @singleton
        class MyClass(<baseClass>):
            pass
        ````
    """
    _instances = {}

    def _getinstance(*args, **kwargs):
        if _class not in _instances:
            _instances[_class] = _class(*args, **kwargs)
        return _instances[_class]

    return _getinstance
