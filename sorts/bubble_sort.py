def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)

# test arr
arr = [10,9,8,7,6,2,4,5]
bubblesort(arr)