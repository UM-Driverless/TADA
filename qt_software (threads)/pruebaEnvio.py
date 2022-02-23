import serial
import random
import time

#se inicia la comunicación con el xbee emisor
coord_serial = serial.Serial(port='COM3', baudrate=9600, bytesize=8, parity='N', stopbits=1)

txt = (str(random.randint(1,100)) + " " + str(random.randint(1,4)) + "\n")
coord_serial.write(txt.encode())
#comprobación de los datos creados
print(txt)