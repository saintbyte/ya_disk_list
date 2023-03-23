from urllib.parse import urlencode

import requests


def download(yandex_path: str, local_path: str, token: str):
    headers = {"Accept": "application/json", "Authorization": f"OAuth {token}"}
    params = {
        "path": yandex_path,
        "fields": "name",
    }
    querystring = urlencode(params)
    url = f"https://cloud-api.yandex.net/v1/disk/resources/download?{querystring}"
    response = requests.get(url, headers=headers)
    down_link_data = response.json()
    try:
        response = requests.get(down_link_data["href"])
    except KeyError:
        print(down_link_data)

    open(local_path, "wb").write(response.content)
