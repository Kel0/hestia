import sys
from functools import partial

from PySide2.QtWidgets import QApplication, QLineEdit, QWidget

from .gui.login import Ui_Form
from .logic import authenticate


class LoginForm:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.form = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.form)

    def _setup(self):
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.ui.pushButton.clicked.connect(
            partial(authenticate, self.ui.lineEdit.text, self.ui.lineEdit_2.text)
        )

    def show(self):
        self.form.show()
        sys.exit(self.app.exec_())
