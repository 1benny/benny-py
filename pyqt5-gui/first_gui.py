#from PyQt6.QtWidgets import QApplication, QWidget, QToolBar, QCheckBox
from PyQt6.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spendings")

        self.label1 = QLabel("My Label", self)


        self.button1 = QPushButton("Change")
        self.button1.setCheckable(True)
        self.button1.clicked.connect(self.b1_clicked)
        self.setCentralWidget(self.button1)
        self.set


    def b1_clicked(self):
        print("Clicked button 1")
        self.button1.setEnabled(False)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

app = QApplication(sys.argv)    ## <~~~ Constructs the application 
window = MainWindow()    ## <~~~ Constructs the window of the program, named "window"
window.show()    ## <~~~ Calls the constructed window to show otherwise remaining hidden 
app.exec()    ## <~~~ Executes the program in a loop