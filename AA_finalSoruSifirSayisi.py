maxZero = 0
numberOfZeros = 0
dizi = [0,1,0,0,0,0,1,1,0,0,0,0,0,1]
for i in range(0, len(dizi)):
    if(dizi[i] == 0):
        numberOfZeros = numberOfZeros + 1
    else:
        if(maxZero < numberOfZeros):
            maxZero = numberOfZeros
        numberOfZeros = 0

print maxZero
