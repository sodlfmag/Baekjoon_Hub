'''
1. dp와 비슷하게 하나씩 쌓아올리기
'''
import sys
t = int(input())

for i in range(t):
    floor = int(sys.stdin.readline().strip())
    room = int(sys.stdin.readline().strip())

    apt = [[0 for j in range(room+1)] for _ in range(floor+1)]

    apt[0] = [j for j in range(room+1)]
 
    for j in range(1, floor+1):
        for k in range(room+1):
            apt[j][k] = sum(apt[j-1][:k+1])
    
    print(apt[floor][room])