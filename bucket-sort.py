#apparently a forbidden algorithm in industry since values in the array need to be within a finite range

def bucket_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    range_arr = max_val - min_val + 1

    arr_counts = [0] * range_arr

    for i in range(len(arr)):
        arr_counts[arr[i] - min_val] += 1

    n = 0
    for i in range(len(arr_counts)):
        for j in range(arr_counts[i]):
            arr[n] = i + min_val
            n += 1
    
    return arr

array = [5,7,6,5]
print(bucket_sort(array))

    