'''
1. 엄지는 상하좌우로 1칸 씩 움직일 수 있음
2. 1 4 7은 왼손 3 6 9는 오른손
3. 2 5 8 0은 더 가까운 엄지손가락을 이용
4. 2 5 8 0에서 거리가 같다면 손잡이손을 사용
5. 주어진 숫자를 누른 손가락을 L R 로 문자열 형태로 누적해 반환

1. 각 손가락의 현재 위치 저장 변수 Ll, Rl
2. 키패드는 3*4 2차원 배열
3. 각 손가락의 인덱스 위치 l_loc, r_loc 배열에 저장
4. 인덱스 각 값의 차이를 통해 거리 계산
5. 키패드의 각 번호는 튜플 값 딕셔너리에 저장
'''
def solution(numbers, hand):
    
    answer = []
    dic = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), 0:(3,1)}
    LB = [1, 4, 7]
    RB = [3, 6, 9]
    CB = [2, 5, 8, 0]
    
    l_loc = [3, 0]
    r_loc = [3, 2]
    
    l_diff = -1
    r_diff = -1
    
    def left_add(i):
        l_loc[0] = dic[numbers[i]][0]
        l_loc[1] = dic[numbers[i]][1]
        answer.append('L')
    
    def right_add(i):
        r_loc[0] = dic[numbers[i]][0]
        r_loc[1] = dic[numbers[i]][1]
        answer.append('R')
    
    for i in range(len(numbers)):
        # 왼손 확정
        if(numbers[i] in LB):
            left_add(i)
        
        # 오른손 확정
        elif(numbers[i] in RB):
            right_add(i)
        
        # 중앙
        else:
            l_diff = abs(l_loc[0] - dic[numbers[i]][0]) + abs(l_loc[1] - dic[numbers[i]][1])
            r_diff = abs(r_loc[0] - dic[numbers[i]][0]) + abs(r_loc[1] - dic[numbers[i]][1])
        
            if(l_diff < r_diff):
                left_add(i)
            elif(l_diff > r_diff):
                right_add(i)
                
            else:
                if(hand == "left"):
                    left_add(i)
                else:
                    right_add(i)
        
        print((l_loc[0],l_loc[1]), (r_loc[0],r_loc[1]))
    return ''.join(answer)