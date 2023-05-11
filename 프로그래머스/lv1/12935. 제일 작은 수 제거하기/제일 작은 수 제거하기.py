def solution(arr):
    flag = int(1e9)
    for val in arr:
        if val < flag:
            flag = val
    arr.remove(flag)
    
    if(len(arr) == 0):
        arr.append(-1)
    return arr