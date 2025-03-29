'''
1. 입력할 때마다 [순번, 순위, [몸무게,키]] 를 입력한다
2. 각 입력별로 전체 비교를 통해 순위를 채워감
3. lambda로 순번별 오름차순 정렬 후 순위 출력 
'''

import sys
n = int(input())

arr = []
w, h = map(int, sys.stdin.readline().split())

arr.append([1, 1, [w, h]])

for i in range(2, n+1):
    w, h = map(int, sys.stdin.readline().split())

    temp = [i, 1, [w, h]]

    for j in range(len(arr)):
        # 덩치가 큰경우
        if(arr[j][2][0] < w and arr[j][2][1] < h):
            arr[j][1] += 1

        # 덩치가 작은경우
        elif(arr[j][2][0] > w and arr[j][2][1] > h):
            temp[1] += 1
        # 덩치가 같은경우
    
    arr.append(temp)

arr.sort(key=lambda x:x[0])

for i in range(len(arr)):
    print(arr[i][1], end=' ')
