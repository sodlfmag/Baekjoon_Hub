'''
1. 0인 번호를 바꿀 수 있음


1. 0을 제외한 다른 숫자가 win_nums에 몇 개 들어있는지 확인 -> 최저 등수
2. 0의 개수만큼 맞춘 수를 추가 -> 최고 등수
'''

def solution(lottos, win_nums):
    cnt = 0
    z_cnt = 0
    arr = []
    for i in range(len(lottos)):
        if(lottos[i] == 0):
            z_cnt += 1
        else:
            arr.append(lottos[i])
    
    for i in range(len(arr)):
        if(arr[i] in win_nums):
            cnt += 1
        
    mins = cnt
    
    best = cnt + z_cnt
    
    answer = []
    if(best >= 2):
        answer.append(7-best)
    else:
        answer.append(6)
        
    if(mins >= 2):
        answer.append(7-mins)
    else:
        answer.append(6)
    

    
    
    return answer