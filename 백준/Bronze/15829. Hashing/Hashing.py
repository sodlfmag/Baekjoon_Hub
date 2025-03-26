'''
1. 배열에 아스키값 저장 (a=1 기준)
2. 반복문을 통해 31의 n승 값을 더함
'''

n = int(input())

s = input() 

arr = list(map(lambda x:ord(x) - ord('a') + 1 , s))

answer = 0
for i in range(len(arr)):
    answer += arr[i] * (31 ** i)

print(answer)