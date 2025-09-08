def quick_sort(arr, s, e):
    if s >= e:
        return arr
    pivot = arr[e]
    insert_ptr = s
    for i in range(s, e):
        if arr[i] <= pivot:
            temp = arr[i]
            arr[i] = arr[insert_ptr]
            arr[insert_ptr] = temp
            insert_ptr += 1

    temp = arr[insert_ptr]
    arr[insert_ptr] = pivot
    arr[e] = temp
    
    quick_sort(arr, s, insert_ptr - 1)
    quick_sort(arr, insert_ptr + 1, e)
    return arr

array = [6,2,4,1,3]
result = quick_sort(array, 0, len(array) - 1)
print(result)