from tkinter import *
import tkinter.scrolledtext as scrolledtext
import serial
import time
import threading
import plotly.graph_objects as go

#coord_serial = serial.Serial(port='COM4', baudrate=9600, bytesize=8, parity='N', stopbits=1)
#end_serial = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1)
#----------RAIZ----------#

#creo una ventana llamada raiz
raiz = Tk()

#pongo un nombre a la ventana
raiz.title("Telemetry")
#establezco un color de fondo
raiz.config(bg = "grey")
#añado un icono
raiz.iconbitmap("coche.ico")
#si quiero que la ventana no pueda ser modificada añado:
#raiz.resizable(0,0)
#elijo el tamaño de la ventana
#raiz.geometry("650x350")

#---------FRAMES---------#


#creamos un frame, lo empaquetamos y lo editamos
velocidad = Frame(raiz)
velocidad.grid(row = 0, column = 0)
velocidad.config(bg = "black")
#velocidad.config(width = "650", height = "350")
#para seleccionar la posicion:
#velocidad.pack(side = "left", anchor = "n")
#añado un borde:
velocidad.config(bd = 15)
velocidad.config(relief = "sunken")
#si quiero que ocupe una parte horizontal de la pantalla:
#velocidad.pack(fill = "x")
#si quiero que ocupe una parte vertical de la pantalla:
#velocidad.pack(fill = "y", expand = "True")
#para editar el cursor:
#velocidad.config(cursor = "hand2")

#añado un titulo para el frame velocidad, si quiero ajustarlo manualmente uso .place, si quiero una posición concreta en el grid ,sticky= "n"
velActualLabel = Label(velocidad, text = "Velocidad actual", fg = "White", bg = "black", font =("Calibri", 14))
velActualLabel.grid(row = 0, column = 0)
#creo la variable velAct
velAct = StringVar()
#creo un cuadro de texto para enviar la información
velActCuadro = Entry(velocidad, textvariable = velAct)
velActCuadro.grid(row = 1, column = 0, padx = 10, pady = 10)
velActCuadro.config(justify = "right")

#Ejemplo a programar
fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 270,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Speed"}))

fig.show()


#velMaxLabel = Label(velocidad, text = "Velocidad maxima", fg = "White", bg = "black", font =("Calibri", 14))
#velMaxLabel.grid(row = 0, column = 1)
#velMax = StringVar()
#velMaxCuadro = Entry(velocidad, textvariable = velMax)
#velMaxCuadro.grid(row = 1, column = 1, padx = 10, pady = 10)
#velMaxCuadro.config(justify = "right")

#ahora creo el frame del estado del DV, con sus accesorios
estado = Frame(raiz)
estado.grid(row = 0, column = 1)
estado.config(bg = "black")
estado.config(bd = 15)
estado.config(relief = "sunken")

estadoLabel = Label(estado, text = "Estado", fg = "White", bg = "black", font =("Calibri", 14))
estadoLabel.grid(row = 0, column = 0)
estadoAct = StringVar()
estadoCuadro = Entry(estado, textvariable = estadoAct)
estadoCuadro.grid(row = 1, column = 0, padx = 10, pady = 10)
estadoCuadro.config(justify = "right")

#frame de los datos brutos
datos = Frame(raiz)
datos.grid(row = 1, column = 0)
datos.config(bg = "black")
datos.config(bd = 15)
datos.config(relief = "sunken")

datosLabel = Label(datos, text = "Datos", fg = "White", bg = "black", font =("Calibri", 14))
datosLabel.grid(row = 0, column = 0)
datosTexto = scrolledtext.ScrolledText(datos, width=30, height=10)
datosTexto.grid(row = 1, column = 0, padx = 10, pady = 10)


#----------BOTON---------#

#programa que escribe los datos recibidos por pantalla
def escribir(rData):
    #se separa la información recibida
    cadena = rData.split(sep = ',')
    velAct.set(cadena[0])
    if cadena[0] > velMax.get():
        velMax.set(cadena[0])
    estadoAct.set(cadena[1])
    datosTexto.insert('1.0', rData)

#creo una variable que indicará si el xbee debe seguir buscando informacion o no
global sigue
sigue = True
#programa que comprueba si se han recibido nuevos datos
def comprobar():
    global sigue
    #datosTexto.insert('1.0', "comprobando datos\n")
    #el programa espera a que el xbee reciba informacion
    if end_serial.in_waiting > 0:
        datosTexto.insert('1.0', "leyendo datos\n")
        #se lee la informacion y se guarda en una variable
        txt = end_serial.readline()
        escribir(txt.decode())
    if sigue == True:
        #se vuelve a llamar al programa si no se ha pedido que pare
        raiz.after(10, comprobar)
    else:
        datosTexto.insert('1.0', "recepcion de datos finalizada\n")

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


#creacion de un frame para organizar botones
botones = Frame(raiz)
botones.grid(row = 1, column = 1)
botones.config(bg = "black")
botones.config(bd = 15)
botones.config(relief = "sunken")

#creo el boton para enviar datos
recibirBoton = Button(botones, text = "Recbir", command = lambda:continuar())
recibirBoton.grid(row = 0, column = 0, padx = 10, pady = 10)
recibirBoton.config(cursor = "hand2")

#creo el boton para cancelar el recibo de datos
pararBoton = Button(botones, text = "Parar", command = lambda:parar())
pararBoton.grid(row = 0, column = 1, padx = 10, pady = 10)
pararBoton.config(cursor = "hand2")

#necesario para que la ventana esté siempre activa
raiz.mainloop()

