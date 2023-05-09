def solution(a, b):
    a, b = min(a,b), max(a,b)
    if(a == b):
        return a
    
    val = 0
    for i in range(a, b+1):
       val += i
    return val