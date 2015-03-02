# -*- coding: cp1254 -*-
from time import time
import random
def maxSubSum1(a):
    seqStart = 0
    seqEnd = -1
    maxSum = 0;
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            thisSum = 0
            for k in range(i,j+1):
                thisSum = thisSum + a[k]
                if(thisSum > maxSum):
                    maxSum = thisSum
                    seqStart = i
                    seqEnd = j
    return {'y0':maxSum, 'y1':seqStart ,'y2':seqEnd }
    

def maxSubSum2(a):
    seqStart = 0
    seqEnd = -1
    maxSum = 0;
    for i in range(0, len(a)):
        thisSum = 0
        for j in range(i, len(a)):
            thisSum = thisSum + a[j]
            if(thisSum > maxSum):
                maxSum = thisSum
                seqStart = i
                seqEnd = j
    return maxSum

def maxSubSum4(a):
    seqStart = 0
    seqEnd = -1
    maxSum = 0;
    thisSum = 0
    i = 0
    for j in range(0, len(a)):
        thisSum = thisSum + a[j]
        if(thisSum > maxSum):
            maxSum = thisSum
            seqStart = i
            seqEnd = j
        elif(thisSum < 0):
            i = j + 1
            thisSum = 0
    return maxSum

if __name__ == '__main__':
    #10 elemanlı dizi zamanları
    a = [4, -3, 5, -2, -1, 2, 6, -2, 7, 10]
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum
    print 'maxSubSum4 zaman = %f' %(t1-t0)

    a = []
    #50 elemanlı dizi zamanları
    for i in range(50):
        x = int(random.uniform(-10, 10))
        a.append(x)
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum
    print 'maxSubSum4 zaman = %f' %(t1-t0)
    a = []
    #100 elemanlı dizi oluşturalım
    for i in range(100):
        x = int(random.uniform(-10, 10))
        a.append(x)
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum
    print 'maxSubSum4 zaman = %f' %(t1-t0)
    a = []
    #500 elemanlı dizi oluşturalım
    for i in range(500):
        x = int(random.uniform(-10, 10))
        a.append(x)
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum
    print 'maxSubSum4 zaman = %f' %(t1-t0)
        
    a = []
    #1000 elemanlı dizi oluşturalım
    for i in range(1000):
        x = int(random.uniform(-10, 10))
        a.append(x)
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum
    print 'maxSubSum4 zaman = %f' %(t1-t0)
    

    a = []
    #10000 elemanlı dizi oluşturalım
    for i in range(10000):
        x = int(random.uniform(-10, 10))
        a.append(x)
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum
    print 'maxSubSum4 zaman = %f' %(t1-t0)

    a = []
    #100000 elemanlı dizi oluşturalım
    for i in range(100000):
        x = int(random.uniform(-10, 10))
        a.append(x)
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum
    print 'maxSubSum4 zaman = %f' %(t1-t0)
