from variables import *
from decoPack import *

def decodificar():
    while (1):
        if (arrayDatos[0] == SOF and datoActual == 0):
            datoActual = 1
            arrayDatos.pop
        elif (arrayDatos[0] == varPack1.id and datoActual == 1):
            if (arrayDatos[11] == EOF):
                pack1(arrayDatos[2:9])
                datoActual = 0
            for i in range(10):
                arrayDatos.pop
        





