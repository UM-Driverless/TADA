from variables import *


def pack1 (pack):

    global rpm
    global ect
    global oilP
    global tps
    global apps
    global breakHdr

    global dvState
    dvState = 101010
    
    rpm = int(str(pack[0])+str(pack[1]))
    ect = int(str(pack[2])+str(pack[3]))
    oilP = int(pack[4])
    tps = int(pack[5])
    apps = int(pack[6])
    breakHdr = int (pack[7])



    # a = varPack1()
    # a.modifyRpm(int(str(pack[0])+str(pack[1])))
    # a.modifyEct(int(str(pack[2])+str(pack[3])))
    # a.modifyOilP(pack[4])
    # a.modifyTps(pack[5])
    # a.modifyApps(pack[6])
    # a.modifyBreakHdr(pack[7])

def pack2 (pack):
    varPack2.modifyDvState(pack[0])