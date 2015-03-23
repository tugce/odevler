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
        
if __name__ == '__main__':
    create()
    
    
