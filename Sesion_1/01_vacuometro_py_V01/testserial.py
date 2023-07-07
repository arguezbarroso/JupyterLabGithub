# Se usa Python2.7
#
#   pip install -r requirements.txt
#
#  apt install python-pip
#
#  pip3 install serial
#
# Prof. Andres Roldan Aranda
# GranaSAT  -  15/01/2020
# https://granasat.ugr.es
#


import serial
import mks925
import binascii
import time



addr = 'COM34'
addr = '/dev/ttyUSB0'
baud =  19200

ser = serial.Serial('/dev/ttyUSB0')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port

