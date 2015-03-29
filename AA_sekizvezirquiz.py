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
        for j in range(0,8):
            if(tablo[i][j] == 1):
                if(sutunKontrol == True): continue
                sutunKontrol = True
                for m in range(0,8):
                    if(tablo[i][m] == 1 and m != j):
                        conf = 'sutun (%d %d) (%d %d) \n' %(i,j,i,m)
                        conflictFirst.append(conf)
            
    for i in range(0,8):
        for j in range(0,8):
            if(tablo[i][j] == 1):
                solCAsagii = i
                solCAsagij = j
                while(solCAsagii != 7 and solCAsagij != 7):
                    solCAsagii = solCAsagii + 1
                    solCAsagij = solCAsagij + 1
                    if(tablo[solCAsagii][solCAsagij] == 1):
                        conf = ' sol asagi capraz(%d %d) (%d %d) \n' %(i,j,solCAsagii,solCAsagij)
                        conflictFirst.append(conf)
                solCYukarii = i
                solCYukarij = j
                while(solCYukarij != 0 and solCYukarii != 0):
                    solCYukarii = solCYukarii - 1
                    solCYukarij = solCYukarij - 1
                    if(tablo[solCYukarii][solCYukarij] == 1):
                        conf = ' sol yukari capraz(%d %d) (%d %d) \n' %(i,j,solCYukarii,solCYukarij)
                        conflictFirst.append(conf)
                sagAsagii = i
                sagAsagij = j
                while(sagAsagii != 7 and sagAsagij != 0):
                    sagAsagii = sagAsagii + 1
                    sagAsagij = sagAsagij -1
                    if(tablo[sagAsagii][sagAsagij] == 1):
                        conf = 'sag asagi capraz (%d %d) (%d %d) \n' %(i, j, sagAsagii, sagAsagij)
                        conflictFirst.append(conf)
                sagYukarii = i
                sagYukarij = j
                while(sagYukarii != 0 and sagYukarij != 7):
                    sagYukarii = sagYukarii - 1
                    sagYukarij = sagYukarij + 1
                    if(tablo[sagYukarii][sagYukarij] == 1):
                        conf = 'sag yukari capraz (%d %d) (%d %d) \n' %(i, j, sagYukarii, sagYukarij)
                        conflictFirst.append(conf)
    for i in range(0, len(conflictFirst)):
        print conflictFirst[i]
    print 'toplam cakisma = %d' % (len(conflictFirst))
    
if __name__ == '__main__':
    t = create()
    test(t)
    
    
    
