import functools
import inspect


def _raiseValueErrorIfErrors(errors: list[str], frmt: str):
    if not errors:
        return
    raise ValueError(frmt.format(", ".join(errors)))


def parametersNotNone(paramNames: list[str]):
    """
    validates that the parameters that are listed are not literally 'None'

    Args:
        paramNames (list[str]): the decorated function parameter names to validate

    Raises:
        ValueError
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            errors = []
            for pn in paramNames:
                if pn in bound.arguments:
                    val = bound.arguments[pn]
                    if val is None:
                        errors.append(pn)
            _raiseValueErrorIfErrors(errors, "Parameter(s) '{}' Cannot Be 'None'")
            return func(*bound.args, **bound.kwargs)

        return wrapper

    return decorator


def parametersHaveTruthyValue(paramNames: list[str]):
    """
    validates that the parameters that are listed all have 'truthy' values

    Args:
        paramNames (list[str]): the decorated function parameter names to validate

    Raises:
        ValueError
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            errors = []
            for pn in paramNames:
                if pn in bound.arguments:
                    val = bound.arguments[pn]
                    if not val:
                        errors.append(pn)
            _raiseValueErrorIfErrors(errors, "Parameter(s) '{}' Are Not A Truthy Value")
            return func(*bound.args, **bound.kwargs)

        return wrapper

    return decorator


def parameterLimit(paramName: str, lo: float | int, hi: float | int):
    """
    validates that the listed parameter's value is within the hi and lo value specified
    and corrects the value keeping it within the range specified

    Args:
        paramName (str): the decorated function parameter name to validate
        lo (float | int): lower value limit
        hi (float | int): upper value limit
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            if paramName in bound.arguments:
                val = bound.arguments[paramName]
                bound.arguments[paramName] = max(lo, min(hi, val))
            return func(*bound.args, **bound.kwargs)

        return wrapper

    return decorator
