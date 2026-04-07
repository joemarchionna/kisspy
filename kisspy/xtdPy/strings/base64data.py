import base64


def fromFile(filename: str) -> str:
    """
    returns a string representing the file contents in Base64

    Args:
        filename (str): the filename of the file to evaluate / convert

    Returns:
        str: the Base64 representation of the file contents
    """
    with open(filename, "rb") as image_file:
        data = base64.b64encode(image_file.read()).decode("utf-8")
    return data


def fromBytes(bytes: bytes) -> str:
    """
    returns a string representing the bytes in Base64

    Args:
        bytes (bytes): bytes from file or stream

    Returns:
        str: the Base64 representation of the bytes
    """
    return base64.b64encode(bytes).decode("utf-8")


def toBytes(base64str: str) -> bytes:
    """
    writes Base64 string back to original binary encoding

    Args:
        base64str (str): the Base64 encoded string

    Returns:
        bytes: binary encoded bytes
    """
    return base64.b64decode(base64str)


def toFile(filename: str, base64str: str):
    """
    writes Base64 string back to original binary encoded file

    Args:
        filename (str): the filename to save the bytes to
        base64str (str): the original Base64 encoded string
    """
    with open(filename, "wb") as writer:
        writer.write(base64.b64decode(base64str))
