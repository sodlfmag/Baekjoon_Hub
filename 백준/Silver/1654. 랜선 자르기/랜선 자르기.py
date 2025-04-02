'''
1. 1~100만 이분탐색
2. 탐색결과 숫자로 나눈 몫의 합이 N보다 크거나 같은 지
'''

import sys

k, n = map(int, input().split())
arr = [0] * k
result = 0
for i in range(k):
    arr[i] = int(sys.stdin.readline().rstrip())

# 이분탐색
start = 1
end = 2**31 -1
while start <= end:
    mid = (start + end)//2
    
    cnt = 0
    for i in range(len(arr)):
        cnt += arr[i] // mid
    
    if(cnt >= n):
        result = mid
        start = mid + 1

    else:
        end = mid - 1

print(result)

