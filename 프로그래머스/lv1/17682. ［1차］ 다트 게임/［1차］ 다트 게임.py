'''
1. S D T 1,2,3 제곱 점수
2. * - 스타상 - 해당 + 이전 점수를 각각 2배로
3. # - 아차상 - 해당 점수를 마이너스
4. 스타상이 처음 나오면 해당 점수만 2배
5. 스타상 중첩 가능
6. 스타상 아차상 중첩 가능
7. S D T는 점수마다 한 개씩 존재
8. 옵션상은 둘 중 하나만 존재 가능, 없을 수도 있음

1. 문자열 단위가 2 또는 3개임 (옵션 존재 유무)
2. isdigit으로 슬라이싱
3. 각 슬라이싱에서 숫자와 제곱으로 우선 점수 계산
4. 옵션 점수 반영
'''


def solution(dartResult):
    answer = 0
    s= 0
    arr = []
    
    for i in range(1, len(dartResult)):
        if(dartResult[i].isdigit()):
            if(dartResult[i] == '0' and dartResult[i-1] == '1'):
                continue
            arr.append(dartResult[s:i])
            s = i
            
    if(dartResult[-1].isalpha()):
        if(dartResult[-2] == '0' and dartResult[-3] == '1'):
            arr.append(dartResult[-3:])
        else:
            arr.append(dartResult[-2:])
    else:
        if(dartResult[-3] == '0' and dartResult[-4] == '1'):
            arr.append(dartResult[-4:])
        else:
            arr.append(dartResult[-3:])
    print(arr)
    
    scores = []
    for i in range(len(arr)):
        # 옵션 점수 존재 시
        if('*' in arr[i] or '#' in  arr[i]):
            score = int(arr[i][:-2])
        # 옵션 점수 부재 시   
        else:
            score = int(arr[i][:-1])
        
        # S,D,T 점수 반영
#         if('S' in arr[i]):
        
        if('D' in arr[i]):
            score = score ** 2
        elif('T' in arr[i]):
            score = score ** 3
            
        scores.append(score)
        
        # 옵션 반영
    for i in range(len(arr)):
        if('*' in arr[i]):
            if(i == 0):
                scores[i] = scores[i] * 2
            else:
                scores[i] = scores[i] * 2
                scores[i-1] = scores[i-1] * 2
        elif('#' in arr[i]):
            scores[i] = -scores[i]
    answer = sum(scores)
    return answer