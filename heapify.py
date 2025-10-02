#this file is to implement the heapify algorithm

def heapify(A):
    n = len(A)

    for i in range((n // 2 - 1), -1, -1):
        sift_down(A, n, i)

def sift_down(A, n, i):
    m = minChildIndex(A, n, i)
    while m < n and A[m] < A[i]:
        swap(A, i, m)
        i = m
        m = minChildIndex(A, n, i)

def minChildIndex(A, n, i):
    left = 2*i + 1
    right = 2*i + 2

    if left >= n:
        return n
    
    if right >= n:
        return left
    else:
        if A[left] < A[right]:
            return left
        else:
            return right
        
def swap(A, i, j):
    A[i], A[j] = A[j], A[i]
        

