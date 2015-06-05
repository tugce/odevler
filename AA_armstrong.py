print "tek for lu cozum"
for i in range(100,999):
    yuzler = i/100
    onlar = (i-yuzler*100)/10
    birler = (i-yuzler*100-onlar*10)
    if(yuzler*yuzler*yuzler + onlar*onlar*onlar + birler*birler*birler == i):
        print "Armastrong sayisi = ",i

#diger yontemle cozum
print "3 for lu cozum"
for i in range(1,9):
    for j in range(0,9):
        for k in range(0,9):
            if(i*100+j*10+k == i*i*i + j*j*j + k*k*k):
                print "Armstrong sayisi = ",i*100+j*10+k
