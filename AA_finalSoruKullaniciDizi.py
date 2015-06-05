# -*- coding: cp1254 -*-
from time import time
import random

dizi = []
diziBoyutu = 1
indis = 0
diziBuyuklugu = input("Dizinin boyutunu giriniz: ")
while(indis <= diziBuyuklugu):
    print "indis ",indis
    print "dizi boyutu ",diziBoyutu
    print "diziBuyuklugu ",diziBuyuklugu
    if(indis < diziBoyutu):
        for i in range(indis,diziBoyutu):
            x = int(random.uniform(-100, 100))
            dizi.append(x)
            indis = indis + 1
    if(diziBoyutu < diziBuyuklugu):
        dizi2=[0 for i in range(diziBoyutu*2)]
        diziBoyutu= diziBoyutu*2
        dizi2 = dizi
        dizi = dizi2
print dizi
print len(dizi)
