'''
1. 스택에 숫자 하나씩 넣기
2. 0이 들어오면 pop
3. 합 구하기
'''

import sys

arr = []
n = int(input())

for i in range(n):
    num = int(sys.stdin.readline().strip())
    if(num == 0):
        arr.pop()  
    else:
        arr.append(num)

print(sum(arr))