def solution(n):
    answer = 0
    cds = []
    for i in range(1, n+1):
        if(n % i == 0):
            cds.append(i)
    
    for v in cds:
        answer += v
    return answer