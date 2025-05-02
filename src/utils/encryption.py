import base64


def encrypt(text):
    if text == "":
        return ""
    return base64.b64encode(text.encode()).decode()


def decrypt(text):
    if text == "":
        return ""
    return base64.b64decode(text.encode()).decode()