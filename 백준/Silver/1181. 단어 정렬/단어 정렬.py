''''
1. 요소 최대 2만개이므로 sort() 사용 가능
2. 집합화를 통해 중복 제거
3. lambda 를 통해 정렬조건 생성
'''

import sys

n = int(sys.stdin.readline().strip())

arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())

arr = list(set(arr))

arr.sort(key=lambda x: (len(x), x))

for i in arr:
    print(i)
