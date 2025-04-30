import base64


def encrypt(text):
    return base64.b64encode(text.encode()).decode()


def decrypt(text):
    return base64.b64decode(text.encode()).decode()