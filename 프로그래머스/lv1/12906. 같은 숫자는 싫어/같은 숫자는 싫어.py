def solution(arr):
    result = []
    key = -1
    for i in range(len(arr)):
        if(arr[i] != key):
            key = arr[i]
            result.append(key)
    return result