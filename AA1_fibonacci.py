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

if __name__ == '__main__':
    number = 10
    for i in range(0,7):
        print fibonacci_loop(number)
        number = number + 10
