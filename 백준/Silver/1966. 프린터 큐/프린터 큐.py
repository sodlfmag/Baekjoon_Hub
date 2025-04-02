'''
1. [기존순번, 중요도] 2차원 배열 생성
2. 딕셔너리 중요도 : 개수 로 저장 -> max로 현재 최대 중요도 사용

'''
import sys
from collections import deque

t = int(input())

for _ in range(t):
    imp_dic = dict()
    n, m = map(int, input().split())
    q = deque()
    imp_list = list(map(int, sys.stdin.readline().split()))
    for i in range(len(imp_list)):
        q.append([i, imp_list[i]])
        if(imp_list[i] in imp_dic):
            imp_dic[imp_list[i]] += 1
        else:
            imp_dic[imp_list[i]] = 1
    
    MAX = max(imp_dic.keys())
    cnt = 1

    while True:
        # 후순위인경우
        if(q[0][1] < MAX):
            temp = q.popleft()
            q.append(temp)
        # 출력하는 경우
        else:
            if(q[0][0] == m):
                print(cnt)
                break
                
            q.popleft()
            cnt += 1
            imp_dic[MAX] -= 1
            if(imp_dic[MAX] == 0):
                del imp_dic[MAX]
                MAX = max(imp_dic.keys())
        