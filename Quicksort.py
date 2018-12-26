

def quicksort(alist):
    quicksort_helper(alist, 0, len(alist) - 1)


def quicksort_helper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quicksort_helper(alist, first, splitpoint - 1)
        quicksort_helper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivot_value = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivot_value:
            leftmark += 1
        while alist[rightmark] >= pivot_value and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark


alist = [54,26,93,17,77,31,44,55,20]
quicksort(alist)
print(alist)
