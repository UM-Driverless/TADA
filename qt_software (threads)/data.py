from variables import *

import serial
end_serial = serial.Serial(port='COM3', baudrate=9600, bytesize=8, parity='N', stopbits=1)

global data
data = []

#programa que escribe los datos recibidos por pantalla
def escribir(rData):
    #se separa la información recibida
    cadena = rData.split(sep = ' ')
    vState.set(str(cadena[0]))
    vSpeed.set(cadena[1])
    return data

#creo una variable que indicará si el xbee debe seguir buscando informacion o no
global sigue
sigue = True
#programa que comprueba si se han recibido nuevos datos
def comprobar():
    txt = ""
    while (1):
        if end_serial.in_waiting > 0 :
            while end_serial.in_waiting > 0 :
        
                #se lee la informacion y se guarda en una variable
                txt = txt + end_serial.read().decode()

            txt2 = txt
            print(txt2)
            escribir(txt2)
            txt = ""
            txt2 = ""
            #end_serial.reset_input_buffer()
    

#funcion que activa el boton recibir que provoca que se empiecen a recibir datos
def continuar():
    global sigue
    sigue = True
    #limpiamos el buffer del xbee
    end_serial.reset_input_buffer()
    comprobar()

#funcion que activa el boton parar que provoca que se deje de buscar informacion
def parar():
    global sigue
    sigue = False