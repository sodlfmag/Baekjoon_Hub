'''
1. 동적으로 게임 시간을 늘려 난이도 조절
2. 실패율 == 도달 but no 클리어 수 / 총 도달 수 
3. 입력 N - 스테이지 수 , stages - 사용자가 멈춰있는 스테이지 번호 배열
4. 실패율이 높은 스테이지부터 '내림차순' 스테이지 번호 담긴 배열 반환
5. 도달한 사람이 없는 경우 실패율 == 0
6. N+1은 모든 스테이지를 클리어한 사람

1. stages를 각 숫자 개수 딕셔너리로 만들기
2. 각 단계의 실패율을 파악할 때 len(stages) - 누적 수 이용
'''


def solution(N, stages):
    dic = {}
    answer = []
    size = len(stages)
    cnt = size 
    for i in range(1, N+2):
        dic[i] = 0
    
    
    for i in range(size):
        dic[stages[i]] += 1
    
    print(dic)
    for i in range(1, N+1):
        if(cnt == 0):
            answer.append([i, 0])
        else:
            answer.append([i, dic[i] / cnt])
            cnt -= dic[i]
            
    answer.sort(key=lambda x : (-x[1], x[0]))
    result = []
    for i in range(len(answer)):
        result.append(answer[i][0])
    
    
    return result