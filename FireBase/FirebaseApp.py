import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.widget = QtWidgets.QStackedWidget()
        self.initUI()
    
    def initUI(self):
        from Login import Login
        mainwindow = Login(self.widget)
        self.widget.addWidget(mainwindow)
        self.widget.setFixedWidth(480)
        self.widget.setFixedHeight(620)
        self.widget.show()
    
    def run(self):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    app = Application()
    app.run()