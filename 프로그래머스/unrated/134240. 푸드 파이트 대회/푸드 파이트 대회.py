# 각 음식의 개수가 짝수인 경우만 그대로, 홀수인 경우는 하나 빼기

def solution(food): 
    answer = ''
    for i in range(1,len(food)):
        if(food[i] % 2 != 0):
            food[i] -= 1
    
    temp = []
    
    for i in range(1, len(food)):
        if(food[i] >= 2):
            temp.append(str(i) * ((food[i]) //2))
    
    s = ''.join(temp)
    answer = s + '0' + s[::-1]
    return answer