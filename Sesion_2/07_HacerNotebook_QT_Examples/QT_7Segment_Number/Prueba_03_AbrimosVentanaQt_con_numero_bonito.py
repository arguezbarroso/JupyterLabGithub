
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout,QLCDNumber
import sys
from PyQt5.QtGui import QIcon

#Añadimos estos recursos para tener la hora del sistema. 
from PyQt5.QtCore import QTime, QTimer



class Window(QDialog):
    def __init__(self):
        super().__init__()
        
        
        #Windows reqerements like geometry,icon and title
        self.setGeometry(200,200,400,200)
        self.setWindowTitle("PyQt5 QLCDNumber")
        #self.setWindowIcon(QIcon("./icon/7segLCD.jpg"))
        self.setWindowIcon(QIcon(".\icon\icons8-formulario-de-entrada-de-números-80.png"))


        timer= QTimer()
        timer.timeout.connect(self.lcd_number)
        
        timer.start(1000) #en ms
        
        self.lcd_number()
        
    def lcd_number(self):
        
        #Creamos un panel para meter el Numero
        vBox=QVBoxLayout()
        
        lcd=QLCDNumber()

        #Vamos a poner el fondo de la pantallita en rojo.
        #estamos modificando una propiedad del StyleSheet del objeto QVBoxLayout, más en: https://doc.qt.io/qtforpython-6/overviews/stylesheet-examples.html
        lcd.setStyleSheet("background-color:red") 
        
        #Añadimos el objeto al panel
        vBox.addWidget(lcd)
        
        time = QTime.currentTime()
        text= time.toString("hh:mm")
        
        lcd.display(text)
        
        self.setLayout(vBox)
        
        
App= QApplication(sys.argv)        
window=Window()
window.show()
sys.exit(App.exec())