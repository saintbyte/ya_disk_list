from urllib.parse import urlencode

import requests


def get_image_list(yadisk_path, token, settings: dict, offset=0):
    headers = {"Accept": "application/json", "Authorization": f"OAuth {token}"}
    params = {
        "limit": settings["ITEMS_LIMIT"],
        "offset": offset,
        "media_type": "image",
    }
    querystring = urlencode(params)
    url = f"https://cloud-api.yandex.net/v1/disk/resources/files?{querystring}"
    if settings["DEBUG"]:
        print(f"url:{url}")
    response = requests.get(url, headers=headers)
    return response.json()


def get_list(path, token, settings):
    # https://yandex.ru/dev/disk/api/reference/all-files.html
    result = []
    page = 0
    while True:
        if settings["DEBUG"]:
            print(f"page:{page}")
        try:
            offset = page * settings["ITEMS_LIMIT"]
            page_result = get_image_list(path, token, settings, offset)
            page = page + 1
        except Exception as e:
            print(str(e))
            return result
        items = page_result["items"]
        if not items:
            if settings["DEBUG"]:
                print(f"items:{items}")
            return result
        result = result + page_result["items"]
