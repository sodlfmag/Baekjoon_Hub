'''
1. 10만개 nlogn -> sort쓰기
2. lambda 조건 2개
'''

import sys

n = int(input())
arr = [None] * n
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr[i] = [x, y]

arr.sort(key=lambda x:(x[0], x[1]))

for i in range(n):
    print(arr[i][0], arr[i][1])