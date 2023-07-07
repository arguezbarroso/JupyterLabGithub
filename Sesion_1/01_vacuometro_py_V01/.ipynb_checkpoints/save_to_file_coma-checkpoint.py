# Se usa Python2.7
#
#   pip install -r requirements.txt
#
#  apt install python-pip
#
#  pip3 install pyserial
#
# Prof. Andres Roldan Aranda
# GranaSAT  -  15/01/2020
# https://granasat.ugr.es
#

#!/usr/bin/python
import serial
import time
import datetime
import mks925



#addr = 'COM34'
addr = '/dev/ttyUSB0'
baud =  19200

vcm_port = serial.Serial(addr, baud,timeout=0,bytesize=8, parity='N', stopbits=1, xonxoff=0, rtscts=0)
print("El puerto del vacuometro es" +str(vcm_port.name))         # check which port was really used

vcm = mks925.MKS925(vcm_port, 123)
print("PResion medida="+str(vcm.read_Pressure()))



f = open('dataFile1.csv','a')

f.write("Date Stamp" + "\t" + "Vacio [mBar]" + "\t"  + "Time Stamp" + "\n")
print(  "Date Stamp" + "\t" + "Vacio [mBar]" + "\t"  + "Time Stamp" + "\n")


for x in range(7200) :
  time_stamp = time.time()
  vacuum_pressure = vcm.read_Pressure()/100
  vacio=('{:.3e}'.format(vacuum_pressure))
  date_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')
  f.write(str(date_stamp) + "," + vacio + ","  + str(time_stamp) + "\n")
  print(str(date_stamp) + "\t" + vacio + "\t"  + str(time_stamp) + "\n")
  f.closed
  time.sleep(10)
  f = open('dataFile.tsv','a')


vcm_port .close()
