#from PyQt6.QtWidgets import QApplication, QWidget, QToolBar, QCheckBox
from PyQt6.QtWidgets import *
import sys

class App(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        
        self.root = QWidget()
        self.root.show()


if __name__ == "__main__":
    app = App()
    app.exec()