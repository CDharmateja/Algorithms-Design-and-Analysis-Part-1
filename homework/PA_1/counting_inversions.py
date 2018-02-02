# Programming Question 1:

# The IntegerArray.txt file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
# Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.
# Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.
# The numeric answer for the given input file should be typed in the space below.
# So if your answer is 1198233847, then just type 1198233847 in the space provided without any spaces or commas or any other punctuation marks. You can make up to 5 attempts.


# Solution:

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
