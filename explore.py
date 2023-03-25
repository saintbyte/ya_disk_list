#!/usr/bin/env python3
from pprint import pprint

import requests
from dotenv import load_dotenv

from repositories.settings import Settings
from ya_disk.auth import auth
from ya_disk.token import get_token
from ya_disk.token import has_authtoken

load_dotenv()


def get_ya_disk_info(settings: dict, token: str) -> dict:
    headers = {"Accept": "application/json", "Authorization": f"OAuth {token}"}
    url = "https://cloud-api.yandex.net/v1/disk/"
    response = requests.get(url, headers=headers)
    return response.json()


def get_ya_trash_resources(settings: dict, token: str) -> dict:
    headers = {"Accept": "application/json", "Authorization": f"OAuth {token}"}
    url = "https://cloud-api.yandex.net/v1/disk/trash/resources/"
    response = requests.get(url, headers=headers)
    return response.json()


def main():
    settings: dict = Settings.get_settings()
    if not settings["YANDEX_CLIENT_ID"]:
        print("create .env file use .env-example as example")
        quit()
    if not has_authtoken():
        auth(settings)
    token = get_token()
    result = get_ya_disk_info(settings, token)
    pprint(result)
    result = get_ya_trash_resources(settings, token)
    pprint(result)


if __name__ == "__main__":
    main()
