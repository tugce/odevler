for i in range(100,999):
    yuzler = i/100
    onlar = (i-yuzler*100)/10
    birler = (i-yuzler*100-onlar*10)
    if(yuzler*yuzler*yuzler + onlar*onlar*onlar + birler*birler*birler == i):
        print "Armastrong sayisi = ",i
