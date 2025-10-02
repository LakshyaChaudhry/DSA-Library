#this file is to implement the heapify algorithm

def heapify(A):
    n = len(A)

    for i in range((n // 2 - 1), 0, -1):
        sift_down(A, n, i)

def sift_down(A, n, i):
    