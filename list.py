#!/usr/bin/env python3
from dotenv import load_dotenv

from repositories.csv_list import CsvImageListRepository
from repositories.settings import Settings
from ya_disk.auth import auth
from ya_disk.list import get_list
from ya_disk.token import get_token
from ya_disk.token import has_authtoken

load_dotenv()

def main():
    settings: dict = Settings.get_settings()
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
