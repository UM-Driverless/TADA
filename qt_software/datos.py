from variables import *
from time import sleep
def datosPantalla(self):
        global primeraVez
        if (primeraVez == 0):
            end_serial.reset_input_buffer()
            primeraVez = 1
        
        global rpm
        global ect
        global oilP
        global tps
        global apps
        global breakHdr


        global arrayDatos
        i = 0
        print("serial: ",end_serial.in_waiting)
        while(end_serial.in_waiting > 0 and i < 12)  :
            #se lee la informacion y se guarda en una variable
            arrayDatos.append(end_serial.read().decode())
            i += 1

    
        global SOF
        global EOF
        datoActual = 0

        while (len(arrayDatos) != 0):
            print("array > 0")
            print(arrayDatos[0])
            if (arrayDatos[0] == SOF and datoActual == 0):
                print("deco SOF")
                datoActual = 1
                arrayDatos.pop(0)
            elif (arrayDatos[0] == varPack1.id and datoActual == 1 and len(arrayDatos) > 10):
                if (arrayDatos[10] == EOF):
                    print("pack1 SOF")
                    pack = arrayDatos[1:9]
                    rpm = int(str(pack[0])+str(pack[1]))
                    ect = int(str(pack[2])+str(pack[3]))
                    oilP = int(pack[4])
                    tps = int(pack[5])
                    apps = int(pack[6])
                    breakHdr = int (pack[7])
                    datoActual = 0
                for i in range(10):
                    arrayDatos.pop(0)
            else:
                arrayDatos.pop(0)


        print(rpm)

        self.lcdRpm.display(rpm)
        self.lcdEct.display(ect)
        self.lcdOilP.display(oilP)
        self.lcdTps.display(tps)
        self.lcdApps.display(apps)
        self.lcdBreakHdr.display(breakHdr)