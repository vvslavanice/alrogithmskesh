'''

Task2

'''

def fib_search(arr, x, n):
    f1 = 0
    f2 = 1
    result = f1 + f2
    while result < n:
        f1 = f2
        f2 = result
        result = f1 + f2
    offset = -1
    while result > 1:
        i = min(offset + f1, n - 1)
        if arr[i] < x:
            result = 2
            f2 = f1
            f1 = result - f2
            offset = i
        elif arr[i] > x:
            result = f1
            f2 = f2 - f1
            f1 = result - f2
        else:
            return i
    if f2 and arr[offset + 1] == x:
        return offset + 1
    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(fib_search(array, 5, len(array) - 1))
print(fib_search(array, 1, len(array) - 1))
print(fib_search(array, 10, len(array) - 1))
