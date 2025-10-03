# Bucket sort works best with uniformly distributed data
# Divides elements into buckets, sorts each bucket, then concatenates

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Determine the number of buckets
    num_buckets = len(arr)
    min_val = min(arr)
    max_val = max(arr)

    # Handle edge case where all elements are the same
    if min_val == max_val:
        return arr

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
    bucket_range = (max_val - min_val) / num_buckets

    for num in arr:
        # Calculate which bucket this element belongs to
        # TODO(human)
        pass

    # Sort individual buckets and concatenate
    sorted_arr = []
    for bucket in buckets:
        # Using insertion sort for each bucket (efficient for small lists)
        sorted_arr.extend(insertion_sort(bucket))

    return sorted_arr


def insertion_sort(arr):
    """Helper function to sort individual buckets"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr



    