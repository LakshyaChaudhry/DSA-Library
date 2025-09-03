
"""This script implemets a binary search algorithm"""
# A good note here is that binary search only works on a pre sorted array
def binary_search(arr, x, l=0, r=None):
    l = 0
    r = len(arr) - 1
    mid = (l + r) // 2

    if r < l:
        return -1
    
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, x, l, mid -1)
    else:
        return binary_search(arr, x, mid+1, r)
    
array = [2, 3, 4, 5, 8]
target = 4

result = binary_search(array, target)
print(result)

# Time complecxity of binary search is O(log n) since it divides the search space by half each comparison