def solution(s):
    answer = []
    dic = {}
    for i in range(26):
        dic[chr(ord('a')+i)] = -1
    
    for i in range(len(s)):
       if(dic[s[i]] == -1):
            dic[s[i]] = i
            answer.append(-1)
       else:
        answer.append(i - dic[s[i]])
        dic[s[i]] = i
                    
    return answer