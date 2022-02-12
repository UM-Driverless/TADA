from variables import varPack1, varPack2


def pack1 (pack):
    varPack1.modifyRpm(int(str(pack[0])+str(pack[1])))
    varPack1.modifyEct(int(str(pack[2])+str(pack[3])))
    varPack1.modifyOilP(pack[4])
    varPack1.modifyTps(pack[5])
    varPack1.modifyApps(pack[6])
    varPack1.modifyBreakHdr(pack[7])

def pack2 (pack):
    varPack2.modifyDvState(pack[0])