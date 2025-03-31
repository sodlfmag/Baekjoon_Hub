'''
1. 루트 N+1까지만 계산
2. 짝수는 제끼기
'''
import math
m, n = map(int, input().split())

# 2까지 선처리
if(m < 3):
    print(2)
    m = 3

for i in range(m, n+1):
    is_prime = True
    if(i % 2 == 0):
        continue
    for j in range(2, int(math.sqrt(i)) + 1):
        if(i % j == 0):
            is_prime = False
            break
    
    if(is_prime):
        print(i)
