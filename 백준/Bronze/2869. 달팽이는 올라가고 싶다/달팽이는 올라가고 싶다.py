'''
1. 오르기/ 내리기 반복되다가 특정 시점에만 오르기로 끝남
2. V-A >= 중간결과가 되는시점이 마지막
'''
import math
A, B, V = map(int, input().split())

mid = (V-A) / (A-B)

# 중간결과 넘어선 경우
if(mid % 1 != 0):
    if(mid * (A-B) >= V):
        print(math.ceil(mid))
    else:
        print(math.ceil(mid) +1)

# 딱 중간결과인 경우
else:
    print(int(mid + 1))

    
    

    