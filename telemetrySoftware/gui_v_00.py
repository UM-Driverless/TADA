from tkinter import *
import tkinter.scrolledtext as scrolledtext
import serial

#coord_serial = serial.Serial(port='COM4', baudrate=9600, bytesize=8, parity='N', stopbits=1)
end_serial = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1)
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

velMaxLabel = Label(velocidad, text = "Velocidad maxima", fg = "White", bg = "black", font =("Calibri", 14))
velMaxLabel.grid(row = 0, column = 1)
velMax = StringVar()
velMaxCuadro = Entry(velocidad, textvariable = velMax)
velMaxCuadro.grid(row = 1, column = 1, padx = 10, pady = 10)
velMaxCuadro.config(justify = "right")

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
    cadena = rData.split(sep = ',')
    velAct.set(cadena[0])
    velMax.set(cadena[1])
    estadoAct.set(cadena[2])
    datosTexto.insert('1.0', rData)

#creo una variable para guardar datos
global rawData
rawData = ""
#programa que comprueba si se han recibido nuevos datos
def comprobar():
    global rawData    
    print("inicio")
    if end_serial.in_waiting > 0:
        print("entra if")
        txt = (end_serial.readline())
        print("txt recibe")
        escribir(txt.decode())

#creo el boton para enviar datos
recibirBoton = Button(raiz, text = "Recbir", command = lambda:comprobar())
recibirBoton.grid(row = 1, column = 1, padx = 10, pady = 10)
recibirBoton.config(cursor = "hand2")



#necesario para que la ventana esté siempre activa
raiz.mainloop()

