from time import time

def fibonacci_loop(counter):
    result = 1
    if(counter == 1 or counter == 2):
        return 1
    i = 3
    temp1 = 1
    temp2 = 1
    result = 1
    while(i <= counter):
        result = temp1 + temp2
        temp1 = temp2
        temp2 = result
        i = i + 1
    return result

def fibonacci_recursive(counter):
    if(counter == 1 or counter == 2):
        return 1
    else: return fibonacci_recursive(counter-1)+fibonacci_recursive(counter-2)
    
if __name__ == '__main__':
    number = 10
    for i in range(0,7):
        t0 = time()
        print fibonacci_loop(number)
        t1 = time()
        print fibonacci_recursive(number)
        t2 = time()
        number = number + 10
        print 'fibonacci_loop zaman = %f' %(t1-t0)
        print 'fibonacci_recursive zaman = %f' %(t2-t1)
