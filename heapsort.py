#this file is for the implementation of the heapsort algorithm

from heapify import heapify, swap, sift_down
#the current implementation is for a min heap and sorts in ascending order -> results in a heapsort of descending order

def heapsort(A):
    n = len(A)
    heapify(A)

    for i in range (n-1, 0, -1):
        swap(A, 0, i)
        n = n-1
        sift_down(A, n, 0)