from hestia.main import LoginForm


class Window:
    def __init__(self, ui):
        ui().show()


def set_window(window=LoginForm):
    Window(window)
