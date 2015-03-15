# -*- coding: cp1254 -*-
from time import time
import random

def maxEleman(dizi):
    maxEleman = dizi[0]
    for i in range(1, len(dizi)):
        if(maxEleman < dizi[i]):
            maxEleman = dizi[i]
    return maxEleman

def maxElemanMerge(dizi):
    dizi = merge(dizi)
    return dizi[len(dizi)-1]

def kEleman(dizi, k):
    dizi = merge(dizi)
    return dizi[k-1]

def merge(dizi):
    if(len(dizi) <=1):
        return dizi
    ortanca = len(dizi)/2
    solDizi = dizi[:ortanca]
    sagDizi = dizi[ortanca:]
    solDizi = merge(solDizi)
    sagDizi = merge(sagDizi)
    dizi = mergeSort(solDizi,sagDizi)
    return dizi

def mergeSort(sol, sag):
    sonuc = []
    solindex = 0
    sagindex = 0
    while solindex < len(sol) and sagindex < len(sag):
        if(sol[solindex] <= sag[sagindex]):
            sonuc.append(sol[solindex])
            solindex = solindex + 1
        else:
            sonuc.append(sag[sagindex])
            sagindex = sagindex + 1

    if sol:
        sonuc.extend(sol[solindex:])
    if sag:
        sonuc.extend(sag[sagindex:])
    return sonuc

if __name__ == '__main__':
    dizi = raw_input('Dizi elemanlarını aralarında birer bosluk bırakarak giriniz: ').split(" ")
    for i in range(0, len(dizi)):
        dizi[i] = int(dizi[i])
    t0 = time()
    print maxEleman(dizi)
    t1 = time()
    print 'maxEleman sure = %f' % (t1-t0)
    t0 = time()
    print maxElemanMerge(dizi)
    t1 = time()
    print 'maxElemanMerge sure = %f' % (t1-t0)
    k = raw_input('Dizinin kaçıncı elemanını istiyorsunuz? ')
    k = int(k)
    t0 = time()
    print kEleman(dizi, k)
    t1 = time()
    print 'kEleman sure = %f' % (t1-t0)
    a = []
    diziBoyutu = input('Kac boyutlu dizi olsun? ')
    #diziboyutu elemanlı dizi zamanları
    for i in range(diziBoyutu):
        x = int(random.uniform(-100, 100))
        a.append(x)
    t0 = time()
    print maxEleman(a)
    t1 = time()
    print 'diziboyutu maxEleman zaman = %f' %(t1-t0)
    t0 = time()
    print maxElemanMerge(a)
    t1 = time()
    print 'diziboyutu maxElemanMerge zaman = %f' %(t1-t0)
    k = raw_input('Dizinin kaçıncı elemanını istiyorsunuz? ')
    k = int(k)
    t0 = time()
    print kEleman(a,k)
    t1 = time()
    print 'diziboyutu kEleman zaman = %f' %(t1-t0)

    a = []
    #50 elemanlı dizi zamanları
    for i in range(50):
        x = int(random.uniform(-100, 100))
        a.append(x)
    t0 = time()
    print maxEleman(a)
    t1 = time()
    print '50 maxEleman zaman = %f' %(t1-t0)
    t0 = time()
    print maxElemanMerge(a)
    t1 = time()
    print '50 maxElemanMerge zaman = %f' %(t1-t0)
    t0 = time()
    print kEleman(a,5)
    t1 = time()
    print '50 kEleman zaman = %f' %(t1-t0)

    a = []
    #100 elemanlı dizi zamanları
    for i in range(100):
        x = int(random.uniform(-100, 100))
        a.append(x)
    t0 = time()
    print maxEleman(a)
    t1 = time()
    print '100 maxEleman zaman = %f' %(t1-t0)
    t0 = time()
    print maxElemanMerge(a)
    t1 = time()
    print '100 maxElemanMErge zaman = %f' %(t1-t0)
    t0 = time()
    print kEleman(a,5)
    t1 = time()
    print '100 kEleman zaman = %f' %(t1-t0)

    a = []
    #1000 elemanlı dizi zamanları
    for i in range(1000):
        x = int(random.uniform(-100, 100))
        a.append(x)
    t0 = time()
    print maxEleman(a)
    t1 = time()
    print '1000 maxEleman zaman = %f' %(t1-t0)
    t0 = time()
    print maxElemanMerge(a)
    t1 = time()
    print '1000 maxElemanMErge zaman = %f' %(t1-t0)
    t0 = time()
    print kEleman(a,5)
    t1 = time()
    print '1000 kEleman zaman = %f' %(t1-t0)

    a = []
    #10000 elemanlı dizi zamanları
    for i in range(10000):
        x = int(random.uniform(-100, 100))
        a.append(x)
    t0 = time()
    print maxEleman(a)
    t1 = time()
    print '10.000 maxEleman zaman = %f' %(t1-t0)
    t0 = time()
    print maxElemanMerge(a)
    t1 = time()
    print '10.000 maxElemanMErge zaman = %f' %(t1-t0)
    t0 = time()
    print kEleman(a,5)
    t1 = time()
    print '10.000 kEleman zaman = %f' %(t1-t0)

    a = []
    #100000 elemanlı dizi zamanları
    for i in range(100000):
        x = int(random.uniform(-100, 100))
        a.append(x)
    t0 = time()
    print maxEleman(a)
    t1 = time()
    print '100.000 maxEleman zaman = %f' %(t1-t0)
    t0 = time()
    print maxElemanMerge(a)
    t1 = time()
    print '100.000 maxElemanMErge zaman = %f' %(t1-t0)
    t0 = time()
    print kEleman(a,5)
    t1 = time()
    print '100.000 kEleman zaman = %f' %(t1-t0)

    a = []
    #1000000 elemanlı dizi zamanları
    for i in range(1000000):
        x = int(random.uniform(-100, 100))
        a.append(x)
    t0 = time()
    print maxEleman(a)
    t1 = time()
    print '1.000.000 maxEleman zaman = %f' %(t1-t0)
    t0 = time()
    print maxElemanMerge(a)
    t1 = time()
    print '1.000.000 maxElemanMErge zaman = %f' %(t1-t0)
    t0 = time()
    print kEleman(a,5)
    t1 = time()
    print '1.000.000 kEleman zaman = %f' %(t1-t0)
