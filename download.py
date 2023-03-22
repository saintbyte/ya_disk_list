#!/usr/bin/env python3
import argparse
import pathlib
from dotenv import load_dotenv

from ya_disk.auth import auth
from ya_disk.list import get_list
from ya_disk.token import get_token
from ya_disk.token import has_authtoken
from repositories.csv_list import CsvImageListRepository
from main import get_settings

load_dotenv()


def main():
    parser = argparse.ArgumentParser(
        prog="downloader.py",
        description="Download image from ya disk",
        epilog="may The Force be with you!")
    parser.add_argument('filename', nargs=1, type=argparse.FileType('r', encoding='UTF-8'))
    parser.add_argument('limit', nargs=1, type=int)
    parser.add_argument('offset', nargs=1, type=int, default=0)
    parser.add_argument('to_dir', nargs=1, type=pathlib.Path)
    parser.parse_args()
    print(parser.filename)
    settings: dict = get_settings()
    if not settings["YANDEX_CLIENT_ID"]:
        print("create .env file use .env-example as example")
        quit()
    if not has_authtoken():
        auth(settings)
    token = get_token()
    repo = CsvImageListRepository(settings=settings)
    repo.save_image_list(result)


if __name__ == "__main__":
    main()
