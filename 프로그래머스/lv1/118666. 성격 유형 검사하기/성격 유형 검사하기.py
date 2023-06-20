'''
1. 4가지 영역에서 2가지 선택지
2. 질문에 대한 7가지 선택지
3. 각 선지별 점수를 합산해 더 큰 쪽이 유형이됨
4. 합산 점수가 0이면 사전 순으로 유형 결정

1. 딕셔너리에 각 값에 대한 점수를 누적
2. 4가지 영역에 상반된 누적값 중 큰 쪽으로 결정
3. 문자열과 점수에 따라 어느쪽에 점수를 부여할 지 결정
'''

def solution(survey, choices):
    dic = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0,}
    score = 0
    result = []
    for i in range(len(survey)):
        if(choices[i] < 4):
            temp = survey[i][0]
            score = 4 - choices[i]
        elif(choices[i] > 4):
            temp = survey[i][1]
            score = choices[i] - 4
        else:
            continue
        
        dic[temp] += score
        
#     if(dic["R"] > dic["T"]):
#         result.append("R")
#     elif(dic["R"] < dic["T"]):
#         result.append("T")
#     else:
#         result.append(min("R", "T"))
        
    def foo(a, b):
        if(dic[a] > dic[b]):
            result.append(a)
        elif(dic[a] < dic[b]):
            result.append(b)
        else:
            result.append(min(a, b))   
            
    foo("R","T")
    foo("C","F")
    foo("J","M")
    foo("A","N")
    
    return ''.join(result)