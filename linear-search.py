

def linear_search(arr, x):
    """ Perform a linear search for x in arr."""
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

array = [5, 3, 8, 4, 2]
target = 4

result = linear_search(array, target)
print(result)

""" Worst case run time for this is O(n) where n is the number of elements in the array"""