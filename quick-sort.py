def quick_sort(arr, s, e):
    if len(arr) <= 1:
        return arr
    pivot = arr[e]
    track_ptr = s
    insert_ptr = s
    for i in range(len(arr) - 1):
        if arr[i] > pivot:
            track_ptr += 1
        if arr[i] <= pivot:
            temp = arr[i]
            arr[i] = arr[insert_ptr]
            arr[insert_ptr] = temp
            insert_ptr += 1
            track_ptr +=1
    
    temp = arr[insert_ptr]
    arr[insert_ptr] = pivot
    pivot = temp
    
    quick_sort(arr, s, insert_ptr - 1)
    quick_sort(arr, insert_ptr + 1, e)
    return arr

array = [6,2,4,1,3]
result = quick_sort(array, 0, len(array) - 1)
print(result)