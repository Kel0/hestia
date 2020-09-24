from typing import Callable

from runner import set_window

from .api import Api
from .session.service import Session


def next_page(operation: str):
    if operation == "auth":
        set_window()


def authenticate(
    get_email: Callable[..., str], get_password: Callable[..., str]
) -> bool:
    api = Api()
    email_value: str = get_email()
    password_value: str = get_password()

    response = api.login(email=email_value, password=password_value)
    try:
        if response["message"].get("session_hash", False):
            Session.create_session(
                email=email_value, session_hash=response["message"]["session_hash"]
            )
            return True
        return False
    except TypeError:
        return False
