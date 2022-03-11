import serial

vComprobar = 0
datoActual = 0
arrayDatos = []
datosRecibidos = 0
end_serial = serial.Serial(port='COM3', baudrate=9600, bytesize=8, parity='N', stopbits=1)

primeraVez = 0

SOF = '\x01'
EOF = '\x04'

#pack1:
varPack1 = '\x01'
rpm = 0
ect = 0
lambd4 = 0

varPack2 = '\x02'
map = 0
fuelPressure = 0
tps = 0
apps = 0

varPack3 = '\x03'
batteryVoltage = 0
breakPreassure = 0
airTemp = 0
OilPreassure = 0

varPack4 = '\x04'
velocidadActual = 0
velocidadObjetivo = 0
anguloActual = 0
anguloObjetivo = 0

varPack5 = '\x05'
frenoActual = 0
frenoObjetivo = 0
motorActual = 0
motorObjetivo = 0

varPack6 = '\x06'
asState = 0
ebsState = 0
missionSelected = 0
steeringState = 0
breakState = 0
lapCounter = 0
conosActuales = 0

varPack7 = '\x07'
asms = 0
goSignal = 0


funcionError = 0