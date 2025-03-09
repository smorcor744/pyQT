from PyQt5.QtWidgets import QDialog

class BaseWindow(QDialog):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget