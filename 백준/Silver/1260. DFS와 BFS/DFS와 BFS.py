from pprint import pprint
from collections import deque
import sys
sys.setrecursionlimit(10**7)

N, M, V = map(int, input().split())
graph = [[]for _ in range(N+1)]

dfs_list = []
dfs_visited = [False] * (N+1)
stack = []
bfs_list = []
bfs_visited = [False] * (N+1)
queue = deque()


def dfs(x):
    dfs_visited[x] = True
    dfs_list.append(x)
    for i in graph[x]:
        if(dfs_visited[i] == False):
            dfs(i)

    # if(dfs_visited[x] == True):
    #     return

    # dfs_visited[x] = True
    # dfs_list.append(x)

    # loc = -1

    # for i in range(len(graph[x])):
    #     if(dfs_visited[graph[x][i]] == False):
    #         loc = graph[x][i]
    #         break

    # if(loc == -1):
    #     return
    # else:
    #     dfs(loc)


def bfs(x):
    if(bfs_visited[x] == True):
        return

    bfs_visited[x] = True
    bfs_list.append(x)

    for i in range(len(graph[x])):
        togo = graph[x][i]
        if(bfs_visited[togo] == False):
            queue.append(togo)

    while(queue):
        togo = queue.popleft()
        bfs(togo)

    else:
        return


for _ in range(M):
    arr, dep = map(int, input().split())
    graph[arr].append(dep)
    graph[dep].append(arr)

for i in range(1, N+1):
    graph[i].sort()

dfs(V)
bfs(V)

print(*dfs_list)
print(*bfs_list)
