
def binary_search(alist, item):
    """
    Takes a list and item as parameter and performs binary search. Returns index position if the item is in the list,
     or -1 if the item is not in the list.
    :param alist: a sorted list
    :param item: the element to be found in the list
    :return: item index if present in list, -1 if item is not present in the list.
    """
    first = 0
    last = len(alist) - 1
    midpoint = (first + last) // 2
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
            return midpoint
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return -1


alist = [1, 3, 5, 8, 10, 17]
print(binary_search(alist, 15))