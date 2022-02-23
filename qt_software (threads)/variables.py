

vComprobar = 0

arrayDatos = []
datosRecibidos = 0




SOF = '8'
EOF = '8'

rpm = 0
ect = 0
oilP = 0
tps = 0
apps = 0
breakHdr = 0

class varPack1:
    id = '1'
    
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

dvState = 0

class varPack2:
    id = '2'

    def modifyDvState(var):
        global dvState
        dvState = var

#pack3
#pack4
#pack5



funcionError = 0