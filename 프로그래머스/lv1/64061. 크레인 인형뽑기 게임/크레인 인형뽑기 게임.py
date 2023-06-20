'''
1. 격자는 N * N 2차원 배열
2. 크레인 작동 줄에 아무것도 없으면 동작 x
3. 배열에 같은 인형 2개가 연속되면 터뜨리기
4. 사라진 인형의 개수를 반환
5. 0은 빈칸, 1~100은 인형 종류

1. 한 번 탐색 시 최악경우 30번의 비교를 수행함 -> 브루트포스
2. 결과 배열을 만들어 항상 마지막 요소 정보만 기록
3. 새로 들어온 요소가 마지막요소와 일치할 경우 pop
4. 마지막 요소 초기화
5. -1일 경우 결과가 빈 상태
6. 터진횟수를 cnt에 누적해 *2
'''
def solution(board, moves):
    cnt = 0
    result = []
    last = -1
    N = len(board)
    for i in range(len(moves)):
        col = moves[i]-1
        for j in range(N):
            # 인형이 존재하면 뽑기
            if(board[j][col] != 0):
                result.append(board[j][col])
                board[j][col] = 0

            # result의 마지막과 비교
                # 터뜨리는 경우
                if(last == result[-1]):
                    result.pop()
                    result.pop()
                    cnt += 1
                    if(len(result) == 0):
                        last = -1
                    else:
                        last = result[-1]
                # 터뜨리지 못하는 경우
                else:
                    last = result[-1]    
                # 인형을 뽑으면 다음 move로 이동
                break

    return  cnt *2