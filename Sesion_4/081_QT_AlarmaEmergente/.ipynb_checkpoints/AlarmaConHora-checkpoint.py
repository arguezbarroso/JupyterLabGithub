#We import the sys module because we want to access the command-line arguments it holds in 
#  the sys.argv list.
import sys

#The time module is imported because we need its sleep() function
import time


#We need the PyQt modules for the GUI and for the QTime class.
# Importamos usando nuestra cabecera de métodos y objetos para QT5
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QAction, QStatusBar
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTime, QTimer



#Every PyQt GUI application must have a QApplication object.
# This object provides access to global-like information such as the application’s directory,
# the screen size (and which screen the application is on, in a multihead system), and so on.
# This object also provides the event loop.

#When we create a QApplication object we pass it the command-line arguments; this is because
# PyQt recognizes some command-line arguments of its own, such as -geometry and -style, 
# so we ought to give it the chance to read them.
# If QApplication recognizes any of the arguments, it acts on them, and removes
# them from the list it was given. The list of arguments that QApplication
# recognizes is given in the QApplication’s initializer’s documentation.

app = QApplication(sys.argv)
try:
    due = QTime.currentTime()
    print(due)
    message = "Alert!"
    if len(sys.argv) < 2:
        print("Atención: faltan argumentos de entrada!")
        raise ValueError
# e application requires a time, so we set the due variable to the time right now.        
    hours, mins = sys.argv[1].split(":")

#Although Python provides its own date and time classes, the PyQt date and time classes are often more convenient
# (and in some respects more powerful), so we tend to prefer them.    
    due = QTime(int(hours), int(mins))

#The hours or minutes are not a valid number, a ValueError will be raised by int(), and if the hours or
# minutes are out of range, due will be an invalid QTime, and we raise a ValueError ourselves.    
    if not due.isValid():
        print("Atención: parece que no has introducido una HH:MM válida!")
        raise ValueError

#If the time is valid,we set the message to be the space-separated concatenation of the other command-line arguments
# if there are any; otherwise,we leave it as the default “Alert!” that we set at the beginning.
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])
# We also provide a default message. If the user has not given at least one command-line argument
# (a time), we raise a ValueError exception. This will result in the time being now and the 
#  message being the “usage” error message.        
except ValueError:
    message = "Usage: alert.pyw HH:MM [optional message]" # 24hr clock


#We loop continuously, comparing the current time with the target time. The loop will terminate if the current time is later 
# than the target time.We could have simply put a pass statement inside the loop, but if we did that Python
# would loop as quickly as possible, gobbling up processor cycles for no good reason. The time.sleep() command tells
# Python to suspend processing for the specified number of seconds, 20 in this case. This gives other programs
# more opportunity to run and makes sense since we don’t want to actually do anything while we wait for the due time to arrive.
while QTime.currentTime() < due:
    time.sleep(20) # 20 seconds
    print("Esperamos que llegue la hora de la alarma")

#A GUI application needs widgets, and in this case we need a label to show the message. A QLabel can acceptHTMLtext, so we
#  give it an HTMLstring that tells it to display bold red text of size 72 points
label = QLabel("<font color=red size=72><b>" + message + "</b></font>")

#In PyQt, any widget can be used as a top-level window, even a button or a label.
# When a widget is used like this, PyQt automatically gives it a title bar. We don’t want a title bar for this application, so we set the label’s window flags to those used for splash screens since they have no title bar. Once we have set up the label that will be our window, we call show() on it. At this point, the label window is not shown! The call to show() merely schedules a “paint event”, that is, it adds a new event to the QApplication object’s event queue that is a request to paint the specified widget.
label.setWindowFlags(Qt.SplashScreen)
label.show()


# Next, we set up a single-shot timer. Whereas the Python library’s time.sleep() function takes a number of seconds, the QTimer.singleShot() function takes a number of milliseconds.We give the singleShot() method two arguments: how long until it should time out (one minute in this case), and a function or method for it to call when it times out.
print("Arrancamos el QTimer de 1 minuto.")
QTimer.singleShot(60000, app.quit) # 1 minute= 60E3 ms = 60 seg = 1 min
app.exec_()