# -*- coding: cp1254 -*-
from time import time
import random

def randomSayiUret():
    x = int(random.uniform(-100, 100))
    return x
dizi = []
diziBoyutu = 1
indis = 0
diziBuyuklugu = input("Dizinin boyutunu giriniz: ")
while(indis < diziBuyuklugu):
    if(diziBoyutu < diziBuyuklugu):
        if(indis < diziBoyutu):
            for i in range(indis,diziBoyutu):
                x = randomSayiUret()
                dizi.append(x)
                indis = indis + 1
        dizi2=[0 for i in range(diziBoyutu*2)]
        diziBoyutu= diziBoyutu*2
        dizi2 = dizi
        dizi = dizi2
    if(diziBoyutu>diziBuyuklugu):
        for i in range(indis,diziBuyuklugu):
            x = randomSayiUret()
            dizi.append(x)
            indis = indis + 1
print dizi
print len(dizi)
