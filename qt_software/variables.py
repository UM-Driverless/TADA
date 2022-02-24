import serial

vComprobar = 0

arrayDatos = []
datosRecibidos = 0
end_serial = serial.Serial(port='COM3', baudrate=9600, bytesize=8, parity='N', stopbits=1)

primeraVez = 0

SOF = 0x01
EOF = 0x04

#pack1:
varPack1 = 0x31
rpm = 0
ect = 0
lambd4 = 0

varPack2 = 0x32
map = 0
fuelPressure = 0
tps = 0
apps = 0

varPack3 = 0x33
batteryVoltage = 0
breakPreassure = 0
airTemp = 0
OilPreassure = 0

varPack4 = 0x34
velocidadActual = 0
velocidadObjetivo = 0
anguloActual = 0
anguloObjetivo = 0

varPack5 = 0x35
frenoActual = 0
frenoObjetivo = 0
motorActual = 0
motorObjetivo = 0

varPack6 = 0x36
asState = 0
ebsState = 0
missionSelected = 0
steeringState = 0
breakState = 0
lapCounter = 0
conosActuales = 0

varPack7 = 0x37
asms = 0
goSignal = 0
pack7 = [varpack7,asms,goSignal]


funcionError = 0