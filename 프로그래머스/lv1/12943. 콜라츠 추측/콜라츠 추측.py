def solution(num):
    cnt = 0
    
    while (cnt < 500):
        if(num == 1):
            return cnt
        
        if(num % 2 == 0):
            num /= 2
        elif(num % 2 == 1):
            num = num *3 +1
        
        cnt += 1
    
    return -1