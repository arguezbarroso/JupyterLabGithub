#Ejemplo muy similar al sacado de: https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/


from PyQt5 import QtWidgets, uic
import sys

#importamos la función generadora del randint: https://www.w3schools.com/python/ref_random_randint.asp
from random import randint

class MainWindow(QtWidgets.QMainWindow):

    #Mainwindow class constructor
    def __init__(self):
        #Call MainWindow super class from PyQt and load the design created in Qt-Designer.
        super(MainWindow, self).__init__()
        uic.loadUi(".\GUI\Gui_Qt_MainWindow.ui",self)
        #Para poner un icono en QtDesigner usamos: https://iconos8.es/

        #Vamos a anclar Evento en el Button con método
        self.button_generator = self.findChild(QtWidgets.QPushButton, 'pushButton') # Find the button
        self.button_generator.clicked.connect(self.rand_generator_pressed) # Remember to pass the definition/method, not the return value!

    def rand_generator_pressed(self):
        random_num=randint(1,300)
        self.lcdNumber.display(random_num)

if __name__ == "__main__":
    
    App= QtWidgets.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(App.exec())