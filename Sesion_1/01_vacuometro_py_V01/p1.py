# Se usa Python3
#
#   pip3 install -r requirements.txt
#
#  apt install python-pip3
#
#  pip3 install pyserial
#
# Prof. Andres Roldan Aranda
# GranaSAT  -  15/01/2020
# https://granasat.ugr.es
#


import serial
import mks925
import binascii
import time


# def read_until(port,finish): 
#     buf = bytearray()
#     while finish  not in buf:
#         buf = buf + port.read() 
#     return buf

# def read_presssure(port,b_addr):
#     port.write(f'@{b_addr}PR1?;FF'.encode('ascii'))
#     data=read_until(port,b';FF').split(b'ACK')[1]
#     data = float(data.split(b';FF')[0].decode('ascii'))
#     return data

#vcm_port = serial.Serial('/dev/tty.usbserial', 19200)

addr = 'COM11'
#addr = '/dev/ttyUSB0'
baud =  19200

vcm_port = serial.Serial(addr, baud,timeout=0,bytesize=8, parity='N', stopbits=1, xonxoff=0, rtscts=0)


vcm = mks925.MKS925(vcm_port, 123)
print(vcm.read_Pressure())




#prueba: para mostrar el mensaje recibido en binario y comparar
# con osciloscopio:
#  print(bin(int.from_bytes('@123PR1?;FF'.encode(),'big')))

