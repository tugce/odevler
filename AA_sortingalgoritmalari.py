# -*- coding: cp1254 -*-
from time import time
import random

def bubbleSort(dizi):
    print 'BUBBLE sort'
    swapSayisi = 0
    comparisonSayisi = 0
    n = len(dizi)
    swapped = False
    while(swapped != True):
        for i in range(n):
            comparisonSayisi = comparisonSayisi + 1
            if(dizi[i-1] > dizi[i]):
                temp = dizi[i-1]
                dizi[i-1] = dizi[i]
                dizi[i] = temp
                swapSayisi = swapSayisi + 1
                swapped = True
    print 'dizi boyutu %d' % n
    print 'swap sayisi %d' % swapSayisi
    print 'comparison sayisi %d' % comparisonSayisi
    
def selectionSort(dizi):
    print 'SELECTION sort'
    max = len(dizi)-1
    comparisonSayisi = 0
    swapSayisi = 0
    nextValue = dizi[max]
    for i in range(max-1,0,-1):
        comparisonSayisi = comparisonSayisi + 1
        if(dizi[i] > nextValue):
            nextValue = dizi[i]
    while((max > 0) and (dizi[max] == nextValue)):
        max = max -1
    while(max > 0):
        value = nextValue
        nextValue = dizi[max]
        for i in range(max-1,0,-1):
            comparisonSayisi = comparisonSayisi + 1
            if(dizi[i] == value):
                swapSayisi = swapSayisi +1
                temp = dizi[i]
                dizi[i] = dizi[max]
                dizi[max] = temp
                max = max - 1
            elif(dizi[i] > nextValue):
                nextValue = dizi[i]
        while((max>0) and (dizi[max] == nextValue)):
              max = max - 1
    n = len(dizi)
    print 'dizi boyutu %d' % n
    print 'swap sayisi %d' % swapSayisi
    print 'comparison sayisi %d' % comparisonSayisi

def insertionSort(dizi):
    print 'INSERTION sort'
    n = len(dizi)
    swapSayisi = 0
    comparisonSayisi = 0
    for i in range(n):
        j = i
        comparisonSayisi = comparisonSayisi + 1
        while((j>0) and dizi[j-1] > dizi[j]):
            comparisonSayisi = comparisonSayisi + 1
            temp = dizi[j-1]
            dizi[j-1] = dizi[j]
            dizi[j] = temp
            swapSayisi = swapSayisi +1
            j = j-1
    print 'dizi boyutu %d' % n
    print 'swap sayisi %d' % swapSayisi
    print 'comparison sayisi %d' % comparisonSayisi
    
def shellSort(dizi):
    print 'SHELL sort'
    swapSayisi = 0
    comparisonSayisi = 0
    n = len(dizi)
    inc = len(dizi) // 2
    while inc:
        for i, el in enumerate(dizi):
            comparisonSayisi = comparisonSayisi + 1
            while i >= inc and dizi[i - inc] > el:
                comparisonSayisi = comparisonSayisi + 1
                swapSayisi = swapSayisi + 1
                dizi[i] = dizi[i - inc]
                i -= inc
            dizi[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    print 'dizi boyutu %d' % n
    print 'swap sayisi %d' % swapSayisi
    print 'comparison sayisi %d' % comparisonSayisi

    
if __name__ == '__main__':
    a = []
    #10 elemanlı dizi zamanları
    for i in range(10):
        x = int(random.uniform(-100, 100))
        a.append(x)
    bubbleSort(a)
    selectionSort(a)
    insertionSort(a)
    shellSort(a)
    
    a = []
    #50 elemanlı dizi zamanları
    for i in range(50):
        x = int(random.uniform(-100, 100))
        a.append(x)
    bubbleSort(a)
    selectionSort(a)
    insertionSort(a)
    shellSort(a)

    a = []
    #100 elemanlı dizi zamanları
    for i in range(100):
        x = int(random.uniform(-100, 100))
        a.append(x)
    bubbleSort(a)
    selectionSort(a)
    insertionSort(a)
    shellSort(a)

    a = []
    #200 elemanlı dizi zamanları
    for i in range(200):
        x = int(random.uniform(-100, 100))
        a.append(x)
    bubbleSort(a)
    selectionSort(a)
    insertionSort(a)
    shellSort(a)

    a = []
    #500 elemanlı dizi zamanları
    for i in range(500):
        x = int(random.uniform(-100, 100))
        a.append(x)
    bubbleSort(a)
    selectionSort(a)
    insertionSort(a)
    shellSort(a)
