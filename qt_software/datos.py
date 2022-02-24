from variables import *
from time import sleep
def datosPantalla(self):
        global primeraVez
        if (primeraVez == 0):
            end_serial.reset_input_buffer()
            primeraVez = 1
            
        i = 0
        while(end_serial.in_waiting > 0 and i < 12)  :
            #se lee la informacion y se guarda en una variable
            arrayDatos.append(end_serial.read())
            print("Nuevo dato: ",arrayDatos)
            i += 1

        datoActual = 0

        while (len(arrayDatos) != 0):
            print("Array while: ", arrayDatos)

            if (arrayDatos[0] == SOF and datoActual == 0):
                print("deco SOF")
                datoActual = 1
                arrayDatos.pop(0)

            if(datoActual == 1 and len(arrayDatos) > 10):
                if (arrayDatos[10] == EOF):
                    if (arrayDatos[0] == varPack1):
                        print("pack1")
                        pack = arrayDatos[1:9]
                        rpm = int(str(pack[3])+str(pack[2])+str(pack[1])+str(pack[0]))
                        ect = int(str(pack[5])+str(pack[4]))
                        lambd4 = int(str(pack[7])+str(pack[6]))
                        for i in range(10):
                            arrayDatos.pop(0)  
                    
                    elif (arrayDatos[0] == varPack2):
                        print("pack2")
                        pack = arrayDatos[1:9]
                        ect = int(str(pack[1])+str(pack[0]))
                        fuelPressure = int(str(pack[3])+str(pack[2]))
                        tps = int(str(pack[5])+str(pack[4]))
                        apps = int(str(pack[7])+str(pack[6]))
                        for i in range(10):
                            arrayDatos.pop(0)
                    
                    elif (arrayDatos[0] == varPack3):
                        
                        print("pack3")
                        pack = arrayDatos[1:9]
                        pack = arrayDatos[1:9]
                        batteryVoltage = int(str(pack[1])+str(pack[0]))
                        breakPreassure = int(str(pack[3])+str(pack[2]))
                        airTemp = int(str(pack[5])+str(pack[4]))
                        OilPreassure = int(str(pack[7])+str(pack[6]))
                        for i in range(10):
                            arrayDatos.pop(0) 
                    
                    elif (arrayDatos[0] == varPack4):
                        print("pack4")
                        pack = arrayDatos[1:9]
                        velocidadActual = int(str(pack[1])+str(pack[0]))
                        velocidadObjetivo = int(str(pack[3])+str(pack[2]))
                        anguloActual = int(str(pack[5])+str(pack[4]))
                        anguloObjetivo = int(str(pack[7])+str(pack[6]))
                        for i in range(10):
                            arrayDatos.pop(0)  
                    
                    elif (arrayDatos[0] == varPack5):
                        print("pack5")
                        pack = arrayDatos[1:9]
                        frenoActual = int(str(pack[1])+str(pack[0]))
                        frenoObjetivo = int(str(pack[3])+str(pack[2]))
                        motorActual = int(str(pack[5])+str(pack[4]))
                        motorObjetivo = int(str(pack[7])+str(pack[6]))
                        for i in range(10):
                            arrayDatos.pop(0)      
                    
                    elif (arrayDatos[0] == varPack6):
                        print("pack6")
                        pack = arrayDatos[1:9]
                        asState = int(str(pack[0]))
                        ebsState = int(str(pack[1]))
                        missionSelected = int(str(pack[2]))
                        steeringState = int(str(pack[3]))
                        breakState = int(str(pack[4]))
                        lapCounter = int(str(pack[5]))
                        conosActuales = int(str(pack[7])+str(pack[6]))
                        for i in range(10):
                            arrayDatos.pop(0)    
                    
                    elif (arrayDatos[0] == varPack7):
                        print("pack7")
                        pack = arrayDatos[1:9]
                        asms = int(str(pack[0]))
                        goSignal = int(str(pack[1]))
                        for i in range(10):
                            arrayDatos.pop(0)  

                arrayDatos.pop(0)
                datoActual = 0

            elif (len(arrayDatos) > 12):
                datoActual = 0
                arrayDatos.pop(0)

            else: break


        self.lcdRpm.display(rpm)
        self.lcdEct.display(ect)
        self.lcdOilP.display(oilP)
        self.lcdTps.display(tps)
        self.lcdApps.display(apps)
        self.lcdBreakHdr.display(breakHdr)

#ascii -> hexa -> dec