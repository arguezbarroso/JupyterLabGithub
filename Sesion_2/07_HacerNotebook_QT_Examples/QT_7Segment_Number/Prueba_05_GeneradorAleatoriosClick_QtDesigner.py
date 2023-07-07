from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

import sys

class MainWindow(QtWidgets.QMainWindow):

    #Mainwindow class constructor
    def __init__(self):
        #Call MainWindow super class from PyQt and load the design created in Qt-Designer.
        QtWidgets.QMainWindow. __init__(self)
        #super(MainWindow, self).__init__()
        self.ui =uic.loadUi(".\GUI\Gui_Qt.ui",self)
        self.setWindowTitle('Audio Analyzer')

        #Aquí empieza el programa principal

if __name__ == "__main__":
    
    App= QtWidgets.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(App.exec())