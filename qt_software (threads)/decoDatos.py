from variables import *
from decoPack import *
from time import sleep

def decodificar():
    global arrayDatos
    global SOF
    global EOF
    global dvState
    global a
    dvState = 5
    datoActual = 0

    while (1):
        if (len(arrayDatos) != 0):
            print("array > 0")
            print(arrayDatos[0])
            sleep(2)
            if (arrayDatos[0] == SOF and datoActual == 0):
                print("deco SOF")
                datoActual = 1
                arrayDatos.pop(0)
            elif (arrayDatos[0] == varPack1.id and datoActual == 1 and len(arrayDatos) > 10):
                if (arrayDatos[10] == EOF):
                    dvState = 5
                    print("pack1 SOF")
                    pack1(arrayDatos[1:9])
                    datoActual = 0
                for i in range(10):
                    arrayDatos.pop(0)
            elif (arrayDatos[0] == varPack2.id and datoActual == 1):
                if (arrayDatos[10] == EOF):
                    pack2(arrayDatos[1:9])
                    datoActual = 0
                for i in range(10):
                    arrayDatos.pop(0)
        





