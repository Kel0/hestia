import json
from typing import Dict, Union

from hestia.api import Api


def _write_json_file(filename: str, data: dict) -> None:
    with open(filename, "w+") as f:
        f.truncate()
        json.dump(data, f, ensure_ascii=False, indent=4)


def _read_json_file(filename: str = "hestia/session/temp/session.json") -> dict:
    with open(filename, "r") as f:
        data: dict = json.load(f)
    return data


class Session:
    def __init__(self):
        self.api = Api()
        self.session_info = _read_json_file()

    @staticmethod
    def create_session(email: str, session_hash: str) -> None:
        _write_json_file(
            filename="hestia/session/temp/session.json",
            data={"email": email, "session_hash": session_hash},
        )

    def user(self) -> Dict[str, Union[str, dict]]:
        user = self.api.get_user(email=self.session_info["email"])
        return user
