import serial
end_serial = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1)

global data
data = []

#programa que escribe los datos recibidos por pantalla
def escribir(rData):
    #se separa la información recibida
    cadena = rData.split(sep = ' ')
    data[0].set(cadena[0])
    data[1].set(cadena[1])
    return data

#creo una variable que indicará si el xbee debe seguir buscando informacion o no
global sigue
sigue = True
#programa que comprueba si se han recibido nuevos datos
def comprobar():
    global sigue
    #el programa espera a que el xbee reciba informacion
    if end_serial.in_waiting > 0:
        #se lee la informacion y se guarda en una variable
        txt = end_serial.readline()
        escribir(txt.decode())
    if sigue == True:
        #se vuelve a llamar al programa si no se ha pedido que pare
        comprobar()

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