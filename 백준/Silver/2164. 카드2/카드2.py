'''
1. deque pop, popleft 시간복잡도 O(1)
2. 최대 연산 50만 * 3 => 150만 -> 브루트포스
'''

from collections import deque

n = int(input())
dq = deque(range(1, n+1))

if(n == 1):
    print(n)
else:
    for i in range(n-1):
        dq.popleft()
        temp = dq.popleft()
        dq.append(temp)

    print(dq[0])