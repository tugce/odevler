# -*- coding: cp1254 -*-
from time import time

def maxEleman(dizi):
    maxEleman = dizi[0]
    for i in range(1, len(dizi)):
        if(maxEleman < dizi[i]):
            maxEleman = dizi[i]
    return maxEleman

def kEleman(dizi, k):
    return dizi[k-1]

if __name__ == '__main__':
    dizi = raw_input('Dizi elemanlarını aralarında birer bosluk bırakarak giriniz: ').split(" ")
    for i in range(0, len(dizi)):
        dizi[i] = int(dizi[i])
    t0 = time()
    print maxEleman(dizi)
    t1 = time()
    print 'maxEleman sure = %f' % (t1-t0)
    k = raw_input('Dizinin kaçıncı elemanını istiyorsunuz? ')
    k = int(k)
    t0 = time()
    print kEleman(dizi, k)
    t1 = time()
    print 'kEleman sure = %f' % (t1-t0)
