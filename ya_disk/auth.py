import webbrowser
from urllib.parse import urlencode

from ya_disk.token import save_token


def input_token():
    token = input("Token:")
    token = token.strip()
    return token


def auth(settings):
    go_auth(settings)
    save_token(input_token())


def go_auth(settings):
    print("Open browser for get token")
    url = "https://oauth.yandex.ru/authorize"
    url_params = {
        "response_type": "token",
        "client_id": settings["YANDEX_CLIENT_ID"],
        "device_id": settings["DEVICE_ID"],
        "device_name": settings["DEVICE_NAME"],
        "redirect_uri": "https://oauth.yandex.ru/verification_code?dev=True",
        "force_confirm": "yes",
        "state": "123",
    }
    querystring = urlencode(url_params)
    url = f"{url}?{querystring}"
    print(f"Opening url (if nothing to do, copy and open in you browser):\n{url}")
    webbrowser.open(url)
