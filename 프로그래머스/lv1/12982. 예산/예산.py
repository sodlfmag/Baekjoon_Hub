def solution(d, budget):
    d.sort()
    cnt = 0
    for i in range(len(d)):
        if(budget >= d[i]):
            cnt += 1
            budget -= d[i]
        else:
            break
    return cnt