INFINITY = float("inf")

def mergesort(arr):
    if len(arr) > 1:
        half = len(arr)//2
        left = arr[:half]
        right = arr[half:]
        mergesort(left)
        mergesort(right)
        merge(arr, left, right)
        return arr


def merge(arr, left, right):
        left.append(INFINITY)
        right.append(INFINITY)
        i,j = 0, 0
        for k in range(len(arr)):
            if left[i] <= right[j]:  # NOTE: This makes merge sort 'stable'
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
