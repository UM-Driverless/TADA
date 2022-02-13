from numpy import array
import serial
from variables import *


def recibo ():

    end_serial = serial.Serial(port='COM3', baudrate=9600, bytesize=8, parity='N', stopbits=1)
    end_serial.reset_input_buffer()
    print("antes")

    global arrayDatos
    global dvState
    dvState = 4

    while (1):
        if end_serial.in_waiting > 0 :
            while end_serial.in_waiting > 0 :
                #se lee la informacion y se guarda en una variable
                
                arrayDatos.append(end_serial.read().decode())

        