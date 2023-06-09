def solution(k, m, score):
    idx = 0
    score.sort()
    result = 0
    for i in range(len(score)):
        if(score[i] > k):
            idx = i
            break
    if(idx > 0):
        arr = score[:idx]
    else:
        arr = score[:]
        
    if(len(arr) < m):
        return 0
    
    arr.reverse()
    for i in range(0,len(arr),m):
        if(len(arr)-i < m):
            break
        result += arr[i+m-1] * m
    return result