def merge(arr, s, m, e):
    left = arr[s: m+1]
    right = arr[m+1: e+1]

    i = 0
    j = 0
    k = s

    while i < len(left) and j < len(right):
        if left [i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, s, e):
    if (e-s) + 1 <= 1:
        return arr
    
    m = (s + e) // 2
    merge_sort(arr, s, m)
    merge_sort(arr, m+1, e)

    merge(arr, s, m, e)
    return arr