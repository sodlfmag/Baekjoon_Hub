def solution(n):
    arr = []
    cnt = 1
    while(n//(3**cnt) > 0):
        cnt += 1
    
    for i in reversed(range(cnt)):
        arr.append(n//(3**i))
        n %= 3**i
    result = 0
    
    for i in range(len(arr)):
        result += arr[i] * (3**i) 

    return result