'''
1. n에 대한 양쪽 절삭 수 계산 - round
2. list 슬라이싱 수행
3. 오른차순 정렬
4. 평균 내고 round
'''

import sys
import math
n = int(input())

if(n == 0):
    print(0)
else:
    arr = [0] * n

    # 절삭 수 계산
    dels = math.floor(n * 0.15 + 0.5)

    for i in range(n):
        arr[i] = int(sys.stdin.readline().rstrip())

    arr.sort()
    if(dels != 0):
        arr = arr[dels : -dels]

    total = sum(arr)
    print(math.floor((total / len(arr)) + 0.5))