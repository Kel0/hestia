import hashlib
from typing import Dict, Union

import requests


def md5(string: str) -> str:
    return hashlib.md5(str.encode(string)).hexdigest()


class Api:
    def login(self, email: str, password: str):
        data: Dict[str, str] = {"email": email, "password": md5(password)}
        response: requests.Response = requests.post(
            url="http://127.0.0.1:8000/api/v1/login", data=data
        )
        return response.json()

    def get_user(self, email: str) -> Dict[str, Dict[str, Union[dict, str, int]]]:
        response: requests.Response = requests.get(
            url="http://127.0.0.1:8000/api/v1/login", params={"email": email}
        )
        return response.json()
