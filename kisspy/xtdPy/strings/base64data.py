import base64


def fromFile(filename):
    """
    returns a string representing the file contents in Base64
    """
    with open(filename, "rb") as image_file:
        data = base64.b64encode(image_file.read()).decode("utf-8")
    return data


def fromBytes(bytes):
    """
    returns a string representing the bytes in Base64
    """
    return base64.b64encode(bytes).decode("utf-8")


def toBytes(base64str):
    """
    writes Base64 string back to original binary encoding
    """
    return base64.b64decode(base64str)


def toFile(filename, base64str):
    """
    writes Base64 string back to original binary encoded file
    """
    with open(filename, "wb") as writer:
        writer.write(base64.b64decode(base64str))
