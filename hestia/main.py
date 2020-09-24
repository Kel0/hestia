import sys
from functools import partial

from typing import Callable

from gui.login import Ui_Form
from PySide2.QtWidgets import QApplication, QLineEdit, QWidget


class LoginForm:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.form = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.form)
        self._setup()

    def _setup(self):
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.ui.pushButton.clicked.connect(
            partial(auth_data, self.ui.lineEdit.text, self.ui.lineEdit_2.text)
        )

    def show(self):
        self.form.show()
        sys.exit(self.app.exec_())


def auth_data(get_username: Callable[..., str], get_password: Callable[..., str]):
    username_value: str = get_username()
    password_value: str = get_password()

    print(username_value, password_value)


def setup_login_form():
    login_form: LoginForm = LoginForm()
    login_form.show()


if __name__ == "__main__":
    setup_login_form()
