def heapsort(arr):
    _build_max_heap(arr)
    print(arr)
    arr_length = len(arr) - 1
    last = arr_length
    for i in range(arr_length, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        last -= 1
        _max_heapify(arr, 0, last)

    return arr

def _max_heapify(arr, i, last):
    left = (2*i)+1
    right = left + 1
    array_length = last

    # check for left
    if left <= array_length and arr[left] > arr[i]:
        largest = left
    else:
        largest = i

    # check for right
    if right <= array_length and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _max_heapify(arr, largest, last)


def _build_max_heap(arr):
    heap_size = len(arr) - 1
    for i in range(heap_size//2, 0, -1):
        _max_heapify(arr, i, heap_size)
