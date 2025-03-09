from PyQt5.QtWidgets import QMainWindow

class BaseWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget