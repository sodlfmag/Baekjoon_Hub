'''
1. 입력된 세 개의 값으로 피타고라스 수행
2. 배열 정렬을 통해 함
3. 0이 들어오며 반복문 종료
4. 시간복잡도: N *(배열 정렬 + 3) -< O(N)
'''

import sys
arr = []
while(True):
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()

    if(arr[0] == 0):
        break

    if(arr[0]**2 + arr[1]**2 == arr[2]**2):
        print('right')
    else:
        print('wrong')