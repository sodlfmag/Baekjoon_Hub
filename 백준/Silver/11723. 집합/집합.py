'''
1. 집합 그대로 구현
'''
import sys
s = set()
all_set = set(map(str, range(20,0,-1)))
m = int(input())

for i in range(m):
    com = sys.stdin.readline().split()
    if(len(com) == 1):
        c = com[0]
    else:
        c = com[0]
        x = com[1]

    match c:
        case 'add':
            s.add(x)
        case 'remove':
            if(x in s):
                s.remove(x)
        case 'check':
            if(x in s):
                print(1)
            else:
                print(0)    
        case 'toggle':
            if(x in s):
                s.remove(x)
            else:
                s.add(x)
        case 'all':
            s = all_set.copy()  
        case 'empty':
            s.clear()