#!/usr/bin/env python3
import os

from dotenv import load_dotenv

from ya_disk.auth import auth
from ya_disk.list import get_list
from ya_disk.token import get_token
from ya_disk.token import has_authtoken
from repositories.csv_list import CsvImageListRepository

load_dotenv()


def get_settings() -> dict:
    """

    :rtype: object
    """
    return {
        "YANDEX_CLIENT_ID": os.environ.get("YANDEX_CLIENT_ID", False),
        "DEVICE_ID": os.environ.get("DEVICE_ID", False),
        "DEVICE_NAME": os.environ.get("DEVICE_NAME", False),
        "ITEMS_LIMIT": int(os.environ.get("ITEMS_LIMIT", 100)),
        "OUTPUT_CSV_FILENAME": os.environ.get("OUTPUT_CSV_FILENAME", "1.csv"),
        "YA_DISK_ROOT": os.environ.get("YA_DISK_ROOT", "disk:/"),
        "DEBUG": os.environ.get("DEBUG", 'False').lower() in ('true', '1', 't'),
    }


def main():
    settings: dict = get_settings()
    if not settings["YANDEX_CLIENT_ID"]:
        print("create .env file use .env-example as example")
        quit()
    if not has_authtoken():
        auth(settings)
    token = get_token()
    result = get_list(settings["YA_DISK_ROOT"], token, settings)
    repo = CsvImageListRepository(settings=settings)
    repo.save_image_list(result)


if __name__ == "__main__":
    main()
