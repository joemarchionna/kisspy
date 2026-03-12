import os
import re

def randomString(size=5) -> str:
    """
    returns a random string of length size

    Args:
        size (int, optional): length of the string returned. Defaults to 5

    Returns:
        str: random string
    """
    return str(os.urandom(size).hex())[:size]

def replaceChars(source: str, remove: str, replaceWith: str = ""):
    """
    cleans and returns a string by replacing / removing chars;\n
    source: str, the source string to clean;\n
    remove: str, string containing any chars to remove from the source string;\n
    replaceWith: str, the string to put in place of any char found, empty (remove) or not empty (replace)
    """
    removeRe = remove.replace("[", r"\[").replace("]", r"\]")
    removeRe = "[{}]".format(removeRe)
    result = re.sub(removeRe, replaceWith, source)
    return result


def cleanAndNormalize(source: str, remove=" %:,[]<>*?", replaceWith: str = "_"):
    """
    cleans a string, works great for a filename
    """
    cfn = replaceChars(source=source, remove=remove, replaceWith=replaceWith)
    if replaceWith:
        endsPattern = "(^" + replaceWith + ")|(" + replaceWith + "$)"
        cfn = re.sub(endsPattern, "", cfn)
        multiPattern = "([" + replaceWith + "]{2})"
        cfn = re.sub(multiPattern, replaceWith, cfn)
    return cfn
