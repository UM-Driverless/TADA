import serial
import random
import time
#se inicia la comunicación con el xbee emisor
coord_serial = serial.Serial(port='COM4', baudrate=9600, bytesize=8, parity='N', stopbits=1)
#end_serial = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1)
i=10000
#bucle que envía datos aleatorios
while i > 0:
    txt = (str(random.randint(1,100)) + "," + str(random.randint(1,4)) + "\n")
    time.sleep(1)
    coord_serial.write(txt.encode())
    print(txt)
    i -= 1