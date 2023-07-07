
#Añadimos el QPushButton
#Aquí se explica cómo usarlo:  https://wiki.qt.io/How_to_Use_QPushButton

from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout,QLCDNumber,QPushButton
import sys

#Añadimos el QFont
from PyQt5.QtGui import QIcon,QFont

#Añadimos estos recursos para tener la hora del sistema. 
from PyQt5.QtCore import QTime, QTimer


#importamos la función generadora del randint: https://www.w3schools.com/python/ref_random_randint.asp
from random import randint


class Window(QDialog):
    def __init__(self):
        super().__init__()
        
        
        #Windows reqerements like geometry,icon and title
        self.setGeometry(200,200,400,200)
        self.setWindowTitle("PyQt5 Random QLCDNumber")
   
        self.setWindowIcon(QIcon(".\icon\icons8-formulario-de-entrada-de-números-80.png"))

        #Creamos un objeto panel para meter el Numero
        vBox=QVBoxLayout()

        self.lcd=QLCDNumber()

        #Vamos a poner el fondo de la pantallita en rojo.
        #estamos modificando una propiedad del StyleSheet del objeto QVBoxLayout, más en: https://doc.qt.io/qtforpython-6/overviews/stylesheet-examples.html
        self.lcd.setStyleSheet("background-color:yellow") 

       #Añadimos el objeto de los números al panel vBox
        vBox.addWidget(self.lcd)

        button= QPushButton("Create random number")
        button.setStyleSheet("background-color:green")
        button.setFont(QFont("Sanserif",14))
        #Con esto conectamos el evento del CLIK a nuestro método de la clase
        button.clicked.connect(self.rand_generator)


       #Añadimos el objeto Botón de pulsar al panel vBox
        vBox.addWidget(button)
        
        self.setLayout(vBox)
        

    def rand_generator(self):
        random_num=randint(1,300)
        self.lcd.display(random_num)

#Creamos un nuevo método que vamos a conectar con el Click del PushButton 
       
App= QApplication(sys.argv)        
window=Window()
window.show()
sys.exit(App.exec())