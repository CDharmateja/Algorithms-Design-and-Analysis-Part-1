def merge_sort(L):
    if len(L) < 2:
        return L[:], 0
    else:
        middle = len(L)//2
        left, linv = merge_sort(L[:middle])
        right, rinv = merge_sort(L[middle:])
        m, split = merge(left, right)
        return m, split+linv+rinv

def merge(left, right):
    result = []
    count = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            count += len(left) - i
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result, count

l = []
file = open('IntegerArray.txt', 'r')
for line in file:
    l.append(int(line))
print(merge_sort(l)[1])
