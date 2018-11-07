
def selectionsort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            min_index = j if arr[j] < arr[min_index]else min_index
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr