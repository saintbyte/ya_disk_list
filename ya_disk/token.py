import os

TOKEN_FILE = ".token"


def has_authtoken() -> bool:
    return os.path.exists(TOKEN_FILE)


def save_token(token):
    fh = open(TOKEN_FILE, "w")
    fh.write(token)
    fh.close()


def get_token():
    with open(TOKEN_FILE, "r") as fh:
        return fh.read()
