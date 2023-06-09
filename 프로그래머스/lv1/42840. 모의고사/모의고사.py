def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5] * 2000
    s2 = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2000
    
    dic = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        if(s1[i] == answers[i]):
            dic[1] += 1
        if(s2[i] == answers[i]):
            dic[2] += 1
        if(s3[i] == answers[i]):
            dic[3] += 1
            
    result = max(dic[1], dic[2], dic[3])
    
    for i in range(1,4):
        if(dic[i] == result):
            answer.append(i)
            
    answer.sort()
    return answer