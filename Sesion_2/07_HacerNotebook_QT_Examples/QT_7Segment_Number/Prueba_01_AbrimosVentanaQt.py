

from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout,QLCDNumber
import sys
from PyQt5.QtGui import QIcon



class Window(QDialog):
    def __init__(self):
        super().__init__()
        
        
        #Windows reqerements like geometry,icon and title
        self.setGeometry(200,200,400,200)
        self.setWindowTitle("PyQt5 QLCDNumber")
        #self.setWindowIcon(QIcon("./icon/7segLCD.jpg"))
        #self.setWindowIcon(QIcon(".\icon\iconQT.png"))
        self.setWindowIcon(QIcon(".\icon\icons8-formulario-de-entrada-de-números-80.png"))
        
       
App= QApplication(sys.argv)        
window=Window()
window.show()
sys.exit(App.exec())
