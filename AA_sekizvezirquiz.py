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
                    print "sol capraz kontrol"
                    solCaprazKontrol = True
                    soli = i
                    solj = j
                    for n in range(0,8):
                        if(soli != 0 and solj!= 0):
                            soli = soli -1
                            solj = solj -1
                            if(tablo[soli][solj] == 1):
                                conf = ' sol capraz(%d %d) (%d %d) \n' %(i,j,soli,solj)
                                conflictFirst.append(conf)
    for i in range(0, len(conflictFirst)):
        print conflictFirst[i]
    
if __name__ == '__main__':
    t = create()
    test(t)
    
    
    
