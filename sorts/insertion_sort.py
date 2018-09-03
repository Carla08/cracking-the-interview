def insertionsort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

    print(arr)

# test arr
arr = [10,9,8,7,6,2,4,5]
insertionsort(arr)
