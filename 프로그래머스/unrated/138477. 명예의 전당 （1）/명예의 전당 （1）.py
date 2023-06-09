def solution(k, score):
    answer = []
    crown = []
    
    if(k >= len(score)):
        for i in range(len(score)):
            crown.append(score[i])
            crown.sort()
            answer.append(crown[0])
    else:
        for i in range(k):
            crown.append(score[i])
            crown.sort()
            answer.append(crown[0])

        for i in range(k, len(score)):
            if(crown[0] < score[i]):
                crown[0] = score[i]
            crown.sort()
            answer.append(crown[0])
    
    print(list(range(3,3)))
    return answer