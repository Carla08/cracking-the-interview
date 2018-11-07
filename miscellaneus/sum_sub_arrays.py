#
# Complete the 'subarraySum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def yield_subarray_of_len(length, arr):
    # arr= [1,2,3,4,5,6]
    # [1][2][3]
    # [1,2], [2,3]
    # [1, 2, 3]
    arr_len = len(arr)
    for i in range(0, arr_len):
        if i + length > arr_len:
            break
        yield arr[i:i + length] # 0,2 #1, 2


def subarraySum(arr):
    # start from arrays len = 1
    # begin sum
    # until creating array of the same len as the original array
    arr_len = len(arr)
    _sum = 0
    for i in range(arr_len):
        for sub_arr in yield_subarray_of_len(2, arr):
            _sum += sum(sub_arr)

    return _sum


print(subarraySum([1,2,3,4,5]))


