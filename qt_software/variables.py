
class Variables():
    def __init__(self):
        self.vComprobar = 0
        self.datoActual = 0
        self.arrayDatos = []
        self.datosRecibidos = 0
        self.puerto = 'COM3'
        self.continuar = 0
        self.primeraVez = 0

        self.SOF = '\x01'
        self.EOF = '\x04'

        #pack1:
        self.varPack1 = '\x01'
        self.rpm = 0
        self.ect = 0
        self.lambd4 = 0

        self.varPack2 = '\x02'
        self.map = 0
        self.fuelPressure = 0
        self.tps = 0
        self.apps = 0

        self.varPack3 = '\x03'
        self.batteryVoltage = 0
        self.breakPreassure = 0
        self.airTemp = 0
        self.OilPreassure = 0

        self.varPack4 = '\x04'
        self.velocidadActual = 0
        self.velocidadObjetivo = 0
        self.anguloActual = 0
        self.anguloObjetivo = 0

        self.varPack5 = '\x05'
        self.frenoActual = 0
        self.frenoObjetivo = 0
        self.motorActual = 0
        self.motorObjetivo = 0

        self.varPack6 = '\x06'
        self.asState = 0
        self.ebsState = 0
        self.missionSelected = 0
        self.steeringState = 0
        self.breakState = 0
        self.lapCounter = 0
        self.conosActuales = 0

        self.varPack7 = '\x07'
        self.asms = 0
        self.goSignal = 0

        self.funcionError = 0