'''
1. lambda 이용해 정렬
'''

n = int(input())
arr = []
import sys  
for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    
    arr.append((i, [age, name]))
    
arr.sort(key=lambda x:(x[1][0], x[0]))

for i in range(n):
    print(arr[i][1][0], arr[i][1][1])
    
    