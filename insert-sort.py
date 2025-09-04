"""This file is for implementing insertion sort algorithm"""

def insertion_sort(arr):
    ptr = 1
    for i in range(0, len(arr)):
        j = ptr
        while arr[j] < arr[j-1] and j > 0:
            temp = arr[j]
            arr[j] = arr[j -1]
            arr[j-1] = temp
            j -= 1
        ptr += 1

# use of a pointer here is easier for understanding the concept which is why i kept it, but i also realize its redundant since we could use "i"