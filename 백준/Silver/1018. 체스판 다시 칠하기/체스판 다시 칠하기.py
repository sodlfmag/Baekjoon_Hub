'''
1. 최대 50X50 리스트
2. 64 * 42 * 42 * 2연산 -> 브루트포스
3. 2개 샘플 보드를 놓고 직접 비교교
'''
import sys
m,n = map(int, input().split())

board = [None] * m

for i in range(m):
    temp = list(sys.stdin.readline().strip())
    board[i] = temp


MIN = 99999

line_a = ['B','W','B','W','B','W','B','W']
line_b = ['W','B','W','B','W','B','W','B']

board_a = []
board_b = []

for i in range(4):
    board_a.append(line_a[:])
    board_a.append(line_b[:])
    board_b.append(line_b[:])
    board_b.append(line_a[:])

for i in range(m-7):
    for j in range(n-7):
        cnt_a = 0
        cnt_b = 0

        for a in range(8):
            for b in range(8):
                if(board[i+a][j+b] != board_a[a][b]):
                    cnt_a += 1
                if(board[i+a][j+b] != board_b[a][b]):
                    cnt_b += 1
        result = min(cnt_a, cnt_b)

        if(MIN > result):
            MIN = result

print(MIN)
    
