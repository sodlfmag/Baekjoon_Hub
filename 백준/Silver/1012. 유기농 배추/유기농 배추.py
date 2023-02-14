import sys
sys.setrecursionlimit(10**6)

def dfs(y, x):
    if(y < 0 or y >= N or x < 0 or x >= M):
        return
    if(graph[y][x] == 1):
        graph[y][x] = 0

        dfs(y-1, x)
        dfs(y+1, x)
        dfs(y, x-1)
        dfs(y, x+1)


T = int(input())
for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if(graph[i][j] == 1):
                cnt += 1
                dfs(i, j)
    print(cnt)
