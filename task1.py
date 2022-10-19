'''

Task 1

'''

def binarysearch(array, item):
    f1 = 0
    #f2 last point
    f2 = len(array) - 1
    middle = (f1 + f2) // 2
    if middle < 0:
        return False
    if array[middle] ==item:
        return True
    if item > array[middle]:
        return binarysearch(array[middle + 1:], item)
    return binarysearch(array[:middle], item)

listofnumber = [1, 2, 3, 4, 5]
elements = -3
somesearch = binarysearch(listofnumber, elements)
print(f'find({elements}): {somesearch}')