#!/usr/bin/env python3
import argparse
import pathlib

from dotenv import load_dotenv

from main import get_settings
from repositories.csv_list import CsvImageListRepository
from ya_disk.auth import auth
from ya_disk.download import download
from ya_disk.token import get_token
from ya_disk.token import has_authtoken

load_dotenv()


def main():
    parser = argparse.ArgumentParser(
        prog="downloader.py",
        description="Download image from ya disk",
        epilog="may The Force be with you!",
    )
    parser.add_argument(
        "--filename",
        nargs=1,
        type=argparse.FileType("r", encoding="UTF-8"),
        help="file with list of ya disk files",
    )
    parser.add_argument(
        "--offset",
        nargs=1,
        type=int,
        default=0,
        help="Starts from",
    )
    parser.add_argument(
        "--limit",
        nargs=1,
        type=int,
        help="count of download from offset",
    )
    parser.add_argument(
        "--to_dir",
        nargs=1,
        type=pathlib.Path,
        help="Where should save files",
    )
    args = parser.parse_args()
    destination_dir = pathlib.Path(args.to_dir[0])
    destination_dir.mkdir(mode=0o777, parents=True, exist_ok=True)
    settings: dict = get_settings()
    if not settings["YANDEX_CLIENT_ID"]:
        print("create .env file use .env-example as example")
        quit()
    if not has_authtoken():
        auth(settings)
    token = get_token()
    repo = CsvImageListRepository(settings=settings)
    files = repo.get_list(args.offset[0], args.limit[0])

    for index, file in enumerate(files):
        print(f"{index}) download: {file['path']}")
        download(file["path"], destination_dir.joinpath(file["name"]), token)


if __name__ == "__main__":
    main()
