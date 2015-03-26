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
                solCAsagii = i
                solCAsagij = j
                while(solCAsagii != 7 and solCAsagij != 7):
                    solCAsagii = solCAsagii + 1
                    solCAsagij = solCAsagij + 1
                    if(tablo[solCAsagii][solCAsagij] == 1):
                        conf = ' sol capraz(%d %d) (%d %d) \n' %(i,j,solCAsagii,solCAsagij)
                        conflictFirst.append(conf)
                solCYukarii = i
                solCYukarij = j
                while(solCYukarij != 0):
                    solCYukarii = solCYukarii - 1
                    solCYukarij = solCYukarij - 1
                    if(tablo[solCYukarii][solCYukarij] == 1):
                        conf = ' sol capraz(%d %d) (%d %d) \n' %(i,j,sagCAsagii,solCYukarij)
                        conflictFirst.append(conf)
                sagCAsagii = i
                sagCAsagij = j
                while(sagCAsagii != 7 and sagCAsagij != 0):
                    sagCAsagii = sagCAsagii + 1
                    sagCAsagij = sagCAsagij - 1
                    if(tablo[sagCAsagii][sagCAsagij] == 1):
                        conf = ' sag capraz(%d %d) (%d %d) \n' %(i,j,sagCAsagii,sagCAsagij)
                        conflictFirst.append(conf)
                sagCYukarii = i
                sagCYukarij = j
                while(sagCYukarii != 0 and sagCYukarij != 7):
                    sagCYukarii = sagCYukarii - 1
                    sagCYukarij = sagCYukarij + 1
                    if(tablo[sagCYukarii][sagCYukarij] == 1):
                        conf = ' sag capraz(%d %d) (%d %d) \n' %(i,j,sagCYukarii,sagCYukarij)
                        conflictFirst.append(conf)
    for i in range(0, len(conflictFirst)):
        print conflictFirst[i]
    
if __name__ == '__main__':
    t = create()
    test(t)
    
    
    
