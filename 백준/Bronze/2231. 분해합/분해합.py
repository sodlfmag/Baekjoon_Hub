'''
1. 연산 최대 100만 * 6 -> 브루트포스
'''

n = int(input())
MIN = 9999999999
for i in  range(1, n+1):
    s = str(i)
    
    temp = 0
    temp += i
    for j in range(len(s)):
        temp += int(s[j])
    
    if(temp == n):
        MIN = min(i, MIN)

if(MIN == 9999999999):
    print(0)    
else:
    print(MIN)