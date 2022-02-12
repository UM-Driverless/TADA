from variables import *
from decoPack import *

def decodificar():
    while (1):
        if (arrayDatos[0] == SOF and datoActual == 0):
            datoActual = 1
            arrayDatos.pop
        elif (arrayDatos[0] == varPack1.id and datoActual == 1):
            if (arrayDatos[10] == EOF):
                pack1(arrayDatos[1:8])
                datoActual = 0
            for i in range(10):
                arrayDatos.pop
        elif (arrayDatos[0] == varPack2.id and datoActual == 1):
            if (arrayDatos[10] == EOF):
                pack2(arrayDatos[1:8])
                datoActual = 0
            for i in range(10):
                arrayDatos.pop
        





