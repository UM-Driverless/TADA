from variables import *
from time import sleep
def datosPantalla(self):
        global primeraVez
        global datoActual
        if (primeraVez == 0):
            end_serial.reset_input_buffer()
            primeraVez = 1
            
        i = 0
        while(end_serial.in_waiting > 0 and i < 12)  :
            #se lee la informacion y se guarda en una variable
            arrayDatos.append((end_serial.read()).decode()) #valores llegan en ascii
            print("Nuevo dato: ", arrayDatos)
            i += 1

        while (len(arrayDatos) != 0):
            print("Array while: ", arrayDatos, "len: ", len(arrayDatos)) 

            if (arrayDatos[0] == SOF and datoActual == 0):
                print("deco SOF")
                print("len: ", len(arrayDatos))
                datoActual = 1
                arrayDatos.pop(0)

            elif(datoActual == 1 and len(arrayDatos) > 10):
                print ("packs")
                if (arrayDatos[10] == EOF):
                    print("deco EOF")
                    if (arrayDatos[0] == varPack1):
                        print("pack1")
                        paquete(self, arrayDatos[1:9], 1) 
                    
                    elif (arrayDatos[0] == varPack2):
                        print("pack2")
                        paquete(self, arrayDatos[1:9], 2)
                    
                    elif (arrayDatos[0] == varPack3):
                        print("pack3")
                        paquete(self, arrayDatos[1:9], 3)
                    
                    elif (arrayDatos[0] == varPack4):
                        print("pack4")
                        paquete(self, arrayDatos[1:9], 4)
                    
                    elif (arrayDatos[0] == varPack5):
                        print("pack5")
                        paquete(self, arrayDatos[1:9], 5)
                    
                    elif (arrayDatos[0] == varPack6):
                        print("pack6")
                        paquete(self, arrayDatos[1:9], 6)
                    
                    elif (arrayDatos[0] == varPack7):
                        print("pack7")
                        paquete(self, arrayDatos[1:9], 7)
                        
                    for i in range(11):
                            arrayDatos.pop(0)  
                    

                else:
                    arrayDatos.pop(0)
                datoActual = 0

            elif (len(arrayDatos) > 12):
                datoActual = 0
                arrayDatos.pop(0)

            else: break

#ascii -> hexa -> dec

def paquete(self, pack, n):
    
    # for i in range(8):

    #     a = ord(pack[i])
    #     print(a)
    #     if (a >= 65):
    #         pack[i] = hex(a - 55)
    #     else:
    #         pack[i] = hex(a - 48)



    if(n == 1):

        rpm = int(pack[3] + pack[2] + pack[1] + pack[0], 16)
        ect = int(pack[5] + pack[4], 16)
        lambd4 = int(pack[7] + pack[6], 16)

        self.rpmO.display(rpm)
        self.ectO.display(ect)
        self.lambdaO.display(lambd4)

    elif(n == 2):
        
        
        ect = int(pack[1] + pack[0])
        fuelPressure = int(pack[3] + pack[2])
        tps = int(pack[5] + pack[4])
        apps = int(pack[7] + pack[6])

        self.mapO.display(map)
        self.fuelPressureO.display(fuelPressure)
        self.tpsO.display(tps)
        self.appsO.display(apps)
    
    elif(n == 3):
        
        batteryVoltage = int(pack[1] + pack[0])
        breakPreassure = int(pack[3] + pack[2])
        airTemp = int(pack[5]  + pack[4])
        OilPreassure = int(pack[7] + pack[6])

        self.batteryVoltageO.display(batteryVoltage)
        self.breakPreassureO.display(breakPreassure)
        self.airTempO.display(airTemp)
        self.oilPressureO.display(OilPreassure)
    
    elif(n == 4):

        velocidadActual = int(pack[1] + pack[0])
        velocidadObjetivo = int(pack[3] + pack[2])
        anguloActual = int(pack[5]+ pack[4])
        anguloObjetivo = int(pack[7]+ pack[6])

        self.velocidadActualO.display(velocidadActual)
        self.velocidadObjetivoO.display(velocidadObjetivo)
        self.anguloActualO.display(anguloActual)
        self.anguloObjetivoO.display(anguloObjetivo)
    
    elif(n == 5):
        
        frenoActual = int(pack[1] + pack[0])
        frenoObjetivo = int(pack[3] + pack[2])
        motorActual = int(pack[5] + pack[4])
        motorObjetivo = int(pack[7] + pack[6])

        self.frenoActualO.display(frenoActual)
        self.frenoObjetivoO.display(frenoObjetivo)
        self.motorActualO.display(motorActual)
        self.motorObjetivoO.display(motorObjetivo)
    
    elif(n == 6):

        asState = int(pack[0])
        ebsState = int(pack[1])
        missionSelected = int(pack[2])
        steeringState = int(pack[3])
        breakState = int(pack[4])
        lapCounter = int(pack[5])
        conosActuales = int(pack[7] + pack[6])

        self.motorObjetivoO.display(motorObjetivo)
        self.ebsStateO.display(ebsState)
        self.missionSelectedO.display(missionSelected)
        self.steeringStateO.display(steeringState)
        self.breakStateO.display(breakState)
        self.lapCounter.display(lapCounter)
        self.conosActualesO.display(conosActuales)
    
    elif(n == 7):
            
        asms = int(pack[0])
        goSignal = int(pack[1])


        self.asmsO.display(asms)
        self.goSignalO.display(goSignal)
