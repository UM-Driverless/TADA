import serial
import random
import time

def envioDatos():
    #se inicia la comunicación con el xbee emisor
    coord_serial = serial.Serial(port='COM4', baudrate=9600, bytesize=8, parity='N', stopbits=1)
    i=10000
    #bucle que envía datos aleatorios
    while i > 0:
        #se crean dos datos aleatorios, uno para la velocidad y otro para el estado del driverless
        txt = (str(random.randint(1,100)) + " " + str(random.randint(1,4)) + "\n")
        time.sleep(1)
        #se envían los datos por los xbee
        coord_serial.write(txt.encode())
        #comprobación de los datos creados
        print(txt)
        i -=1