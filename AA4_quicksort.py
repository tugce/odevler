def quickSort(arr,counter):
    less = []
    pivotList = []
    more = []
    counter = counter + 1
    if len(arr) <= 1:
        counter = counter + 1
        return arr
    else:
        pivot = arr[0]
        counter = counter + 1
        for i in arr:
            if i < pivot:
                counter = counter + 1
                less.append(i)
            elif i > pivot:
                counter = counter + 1
                more.append(i)
            else:
                counter = counter + 1
                pivotList.append(i)
        less = quickSort(less,counter)
        counter = counter + 1
        more = quickSort(more,counter)
        counter = counter + 1
        sonuc = []
        sonuc.extend(less)
        sonuc.extend(pivotList)
        sonuc.extend(more)
        return {'dizi':sonuc, 'count':counter}
 
a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
print a
counter = 0
print len(a)
a = quickSort(a ,counter)
print a
