def quicksort(arr, first, last):
    if first < last:
        partition_index = _partition(arr, first, last)
        quicksort(arr, first, partition_index - 1)
        quicksort(arr, partition_index + 1, last)

    print(arr)


def _partition(arr, first, partition_index):
    partition = arr[partition_index]
    i = first - 1
    for j in range(first, partition_index):
        if arr[j] <= partition:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap
    arr[i + 1], arr[partition_index] = arr[partition_index], arr[i + 1]  # swap
    return i + 1


# test arr
arr = [10,9,8,7,6,2,4,5]
quicksort(arr, 0, len(arr) - 1)
