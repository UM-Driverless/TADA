import serial
end_serial = serial.Serial

def datosPantalla(self):
        global primeraVez
        if (primeraVez == 0):
            end_serial.reset_input_buffer()
            primeraVez = 1

        i = 0
        while(end_serial.in_waiting > 0 and i < 12)  :
            #se lee la informacion y se guarda en una variable
            self.variables.arrayDatos.append((end_serial.read())) #valores llegan en ascii
            print("Nuevo dato: ", self.variables.arrayDatos)
            i += 1

        while (len(self.variables.arrayDatos) != 0):
            print("Array while: ", self.variables.arrayDatos, "len: ", len(self.variables.arrayDatos))

            if (self.variables.arrayDatos[0].decode() == self.variables.SOF and datoActual == 0):
                print("deco SOF")
                print("len: ", len(self.variables.arrayDatos))
                self.variables.datoActual = 1
                self.variables.arrayDatos.pop(0)

            elif(self.variables.datoActual == 1 and len(self.variables.arrayDatos) > 10):
                print ("packs")
                if (self.variables.arrayDatos[10].decode() == self.variables.EOF):
                    print("deco EOF")
                    if (self.variables.arrayDatos[0].decode() == self.variables.varPack1):
                        print("pack1")
                        paquete(self, self.variables.arrayDatos[1:9], 1)

                    elif (self.variables.arrayDatos[0].decode() == self.variables.varPack2):
                        print("pack2")
                        paquete(self, self.variables.arrayDatos[1:9], 2)

                    elif (self.variables.arrayDatos[0].decode() == self.variables.varPack3):
                        print("pack3")
                        paquete(self, self.variables.arrayDatos[1:9], 3)

                    elif (self.variables.arrayDatos[0].decode() == self.variables.varPack4):
                        print("pack4")
                        paquete(self, self.variables.arrayDatos[1:9], 4)

                    elif (self.variables.arrayDatos[0].decode() == self.variables.varPack5):
                        print("pack5")
                        paquete(self, self.variables.arrayDatos[1:9], 5)

                    elif (self.variables.arrayDatos[0].decode() == self.variables.varPack6):
                        print("pack6")
                        paquete(self, self.variables.arrayDatos[1:9], 6)

                    elif (self.variables.arrayDatos[0].decode() == self.variables.varPack7):
                        print("pack7")
                        paquete(self, self.variables.arrayDatos[1:9], 7)

                    for i in range(11):
                            self.variables.arrayDatos.pop(0)


                else:
                    self.variables.arrayDatos.pop(0)
                self.variables.datoActual = 0

            elif (len(self.variables.arrayDatos) > 12):
                self.variables.datoActual = 0
                self.variables.arrayDatos.pop(0)

            else: break

#ascii -> hexa -> dec

def paquete(self, pack, n):

    for i in range(len(pack)):

        a = ord(pack[i].decode())
        print(a)
        if (a >= 65):
            pack[i] = str(a - 55)
        else:
            pack[i] = str(a - 48)

    print("decoded pack: ", pack)

    if(n == 1):

        rpm = int(pack[3] + pack[2] + pack[1] + pack[0], 16)
        ect = int(pack[5] + pack[4], 16)
        lambd4 = int(pack[7] + pack[6], 16)

        self.rpmO.display(rpm)
        self.ectO.display(ect)
        self.lambdaO.display(lambd4)

    elif(n == 2):


        map = int(pack[1] + pack[0], 16)
        fuelPressure = int(pack[3] + pack[2], 16)
        tps = int(pack[5] + pack[4], 16)
        apps = int(pack[7] + pack[6], 16)

        self.mapO.display(map)
        self.fuelPressureO.display(fuelPressure)
        self.tpsO.display(tps)
        self.appsO.display(apps)

    elif(n == 3):

        batteryVoltage = int(pack[1] + pack[0])
        breakPreassure = int(pack[3] + pack[2], 16)
        airTemp = int(pack[5]  + pack[4], 16)
        OilPreassure = int(pack[7] + pack[6], 16)

        self.batteryVoltageO.display(batteryVoltage)
        self.breakPreassureO.setValue(breakPreassure)
        self.airTempO.display(airTemp)
        self.oilPressureO.display(OilPreassure)

    elif(n == 4):

        velocidadActual = int(pack[1] + pack[0], 16)
        velocidadObjetivo = int(pack[3] + pack[2], 16)
        anguloActual = int(pack[5]+ pack[4], 16)
        anguloObjetivo = int(pack[7]+ pack[6], 16)

        self.velocidadActualO.display(velocidadActual)
        self.velocidadObjetivoO.display(velocidadObjetivo)
        self.anguloActualO.display(anguloActual)
        self.anguloObjetivoO.display(anguloObjetivo)

    elif(n == 5):

        frenoActual = int(pack[1] + pack[0], 16)
        frenoObjetivo = int(pack[3] + pack[2], 16)
        motorActual = int(pack[5] + pack[4], 16)
        motorObjetivo = int(pack[7] + pack[6], 16)

        self.frenoActualO.setValue(frenoActual)
        self.frenoObjetivoO.setValue(frenoObjetivo)
        self.motorActualO.display(motorActual)
        self.motorObjetivoO.display(motorObjetivo)

    elif(n == 6):

        asState = int(pack[0], 16)
        ebsState = int(pack[1], 16)
        missionSelected = int(pack[2], 16)
        steeringState = int(pack[3], 16)
        breakState = int(pack[4], 16)
        lapCounter = int(pack[5], 16)
        conosActuales = int(pack[7] + pack[6], 16)

        self.asStateO.display(asState)
        self.motorObjetivoO.display(motorObjetivo)
        self.ebsStateO.display(ebsState)
        self.missionSelectedO.display(missionSelected)
        self.steeringStateO.display(steeringState)
        self.breakStateO.display(breakState)
        self.lapCounterO.display(lapCounter)
        self.conosActualesO.display(conosActuales)

    elif(n == 7):

        asms = int(pack[0], 16)
        goSignal = int(pack[1], 16)


        self.asmsO.display(asms)
        self.goSignalO.display(goSignal)
