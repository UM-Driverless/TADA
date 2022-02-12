vSpeed = 0
vState = 0

vComprobar = 0

arrayDatos = []
datosRecibidos = 0

datoActual = 0


SOF = 0000
EOF = 1111

rpm = 0
ect = 0
oilP = 0
tps = 0
apps = 0
breakHdr = 0

class varPack1:
    id = 1

    def modifyRpm(var):
        global rpm
        rpm = var

    def modifyEct(var):
        global ect
        ect = var

    def modifyOilP(var):
        global oilP
        oilP = var

    def modifyTps(var):
        global tps
        tps = var

    def modifyApps(var):
        global apps
        apps = var

    def modifyBreakHdr(var):
        global breakHdr
        breakHdr = var

    







#pack2
#pack3
#pack4
#pack5



funcionError = 0