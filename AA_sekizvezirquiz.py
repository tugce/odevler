import random

def create():
    satranc = [[0 for x in range(8)] for x in range(8)]
    for i in range(0,8):
        birVar = False
        for j in range(0,8):
            x = int(random.uniform(0, 2))
            if(x == 0):
                if(j == 7 and birVar == False):
                    satranc[j][i] = 1
                    birVar = True
                else:
                    satranc[j][i] = 0
            elif(x == 1):
                if(birVar == False):
                    satranc[j][i] = 1
                    birVar = True
                else:
                    satranc[j][i] = 0
    for i in range(0,8):
        print satranc[i]
    return satranc
def test(tablo):
    conflictFirst = []
    conflictSecond = []
    for i in range(0,8):
        sutunKontrol = False
        solCaprazKontrol = False
        sagCaprazKontrol = False
        for j in range(0,8):
            if(tablo[i][j] == 1):
                if(sutunKontrol == True): continue
                sutunKontrol = True
                for m in range(0,8):
                    if(tablo[i][m] == 1 and m != j):
                        conf = 'sutun (%d %d) (%d %d) \n' %(i,j,i,m)
                        conflictFirst.append(conf)
            if(tablo[i][j] == 1):
                if(solCaprazKontrol == False):
                    solCaprazKontrol = True
                    soliy = i
                    soljy = j
                    solia = i
                    solja = j
                    for n in range(0,8):
                        if(soliy != 0 or soljy!= 0):
                            soliy = soliy -1
                            soljy = soljy -1
                            if(tablo[soliy][soljy] == 1):
                                conf = ' sol capraz(%d %d) (%d %d) \n' %(i,j,soliy,soljy)
                                conflictFirst.append(conf)
                        elif(solia != 7 or solja != 7):
                            solia = solia + 1
                            solja = solja + 1
                            if(tablo[solia][solja] == 1):
                                conf = ' sol capraz(%d %d) (%d %d) \n' %(i,j,solia,solja)
                                conflictFirst.append(conf)  
                if(sagCaprazKontrol == False):
                    sagCaprazKontrol = True
                    sagiy = i
                    sagjy = j
                    sagia = i
                    sagja = j
                    for n in range(0,8):
                        if(sagiy != 0 and sagjy!= 7):
                            sagiy = sagiy -1
                            sagjy = sagjy +1
                            if(tablo[sagiy][sagjy] == 1):
                                conf = ' sag capraz(%d %d) (%d %d) \n' %(i,j,sagiy,sagjy)
                                conflictFirst.append(conf)
                        elif(sagia != 7 and sagja!= 0):
                            sagia = sagia +1
                            sagja = sagja -1
                            if(tablo[sagia][sagja] == 1):
                                conf = ' sag capraz(%d %d) (%d %d) \n' %(i,j,sagia,sagja)
                                conflictFirst.append(conf)
    for i in range(0, len(conflictFirst)):
        print conflictFirst[i]
    
if __name__ == '__main__':
    t = create()
    test(t)
    
    
    
