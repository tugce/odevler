def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    print "left = ",left
    right = m[middle:]
    print "right = ",right
    print "sol rekursif"
    left = merge_sort(left)
    print "sag rekursif"
    right = merge_sort(right)
    return list(merge(left, right))

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    print "result = ",result
    return result
if __name__ == '__main__':
    dizi = [4,2,8,5,3,7,2,6,3,5,3,5]
    print dizi
    sonuc = merge_sort(dizi)
    print sonuc
