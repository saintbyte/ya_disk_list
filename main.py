#!/usr/bin/env python3
import os
import webbrowser
from urllib.parse import urlencode

import requests
from dotenv import load_dotenv

load_dotenv()

SETTINGS = {
    "YANDEX_CLIENT_ID": os.environ.get("YANDEX_CLIENT_ID", False),
    "DEVICE_ID": os.environ.get("DEVICE_ID", False),
    "DEVICE_NAME": os.environ.get("DEVICE_NAME", False),
    "ITEMS_LITIT": os.environ.get("ITEMS_LITIT", 100),
    "OUTPUT_CSV_FILENAME": os.environ.get("OUTPUT_CSV_FILENAME", "1.csv"),
    "YA_DISK_ROOT": os.environ.get("YA_DISK_ROOT", "disk:/"),
}

TOKEN_FILE = ".token"


def has_authtoken() -> bool:
    return os.path.exists(TOKEN_FILE)


def save_token(token):
    fh = open(TOKEN_FILE, "w")
    fh.write(token)
    fh.close()


def input_token():
    token = input("Token:")
    token = token.strip()
    return token


def get_token():
    with open(TOKEN_FILE, "r") as fh:
        return fh.read()


def auth():
    go_auth()
    save_token(input_token())


def go_auth():
    print("Open browser for get token")
    url = "https://oauth.yandex.ru/authorize"
    url_params = {
        "response_type": "token",
        "client_id": SETTINGS["YANDEX_CLIENT_ID"],
        "device_id": SETTINGS["DEVICE_ID"],
        "device_name": SETTINGS["DEVICE_NAME"],
        "redirect_uri": "https://oauth.yandex.ru/verification_code?dev=True",
        "force_confirm": "yes",
        "state": "123",
    }
    querystring = urlencode(url_params)
    url = f"{url}?{querystring}"
    print(f"Opening url (if nothing to do, copy and open in you browser):\n{url}")
    webbrowser.open(url)


def get_files_list(yadisk_path, token, offset=0):
    headers = {"Accept": "application/json", "Authorization": f"OAuth {token}"}
    params = {
        "limit": SETTINGS["ITEMS_LITIT"],
        "offset": offset,
        "media_type": "image",
    }
    querystring = urlencode(params)
    url = f"https://cloud-api.yandex.net/v1/disk/resources/files?{querystring}"
    response = requests.get(url, headers=headers)
    return response.json()


def get_list(path, token):
    # https://yandex.ru/dev/disk/api/reference/all-files.html
    result = []
    page = 0
    while True:
        print(f"page:{page}")
        try:
            offset = page * SETTINGS["ITEMS_LITIT"]
            page_result = get_files_list(path, token, offset)
            page = page + 1
        except Exception as e:
            print(str(e))
            return result
        items = page_result["items"]
        if not items:
            return result
        result = result + page_result["items"]


def main():
    if not SETTINGS["YANDEX_CLIENT_ID"]:
        print("create .env file use .env-example as example")
        quit()
    if not has_authtoken():
        auth()
    token = get_token()
    result = get_list(SETTINGS["YA_DISK_ROOT"], token)
    fh = open(SETTINGS["OUTPUT_CSV_FILENAME"], "w")
    for file in result:
        s = f"{file['path']};{file['name']};{file['size']};{file['sha256']};\n"
        fh.write(s)
    fh.close()


if __name__ == "__main__":
    main()
