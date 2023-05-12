def solution(number):
    length = len(number)
    cnt = 0
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                if(number[i] + number[j] + number[k] == 0):
                    cnt += 1
    return cnt