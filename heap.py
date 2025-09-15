import heapq

def heap_push(heap, item):
    heapq.heappush(heap, item)
    return heap

def heap_pop(heap):
    return heapq.heappop(heap) if heap else None

def heap_peek(heap):
    return heap[0] if heap else None

#code below is for the heap top k problem
def find_k_largest(nums, k):
    if k > len(nums):
        return None
    heap = []
    for num in nums:
        heap_push(heap, num)
        if len(heap) > k:
            heap_pop(heap)
    return heap

numbers = [3,2,1,5,6,4]
print(find_k_largest(numbers, 2))
