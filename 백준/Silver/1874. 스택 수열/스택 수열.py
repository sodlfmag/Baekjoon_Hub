'''
1. 순서가 
'''\

'''
1 2 3 4
1 2 3 - 4
1 2 - 4 3
1 2 5 - 4 3
1 2 5 6 - 4 3
1 2 5 - 4 3 6
1 2 5 7 - 4 3 6
1 2 5 7 8 - 4 3 6

 
'''


import sys
n = int(input())
seq = [0] * n
stack = []
logs = []
candy = list(range(n, 0, -1))

def push():
    stack.append(candy.pop())

def pop():
    stack.pop()

for i in range(n):
    seq[i] = int(sys.stdin.readline().rstrip())


idx = 0
is_possible = True

while(idx < len(seq)):
    #push 해야하는 경우
    if(not stack or stack[-1] < seq[idx]):
        stack.append(candy.pop())
        logs.append('+')

    #pop 해야하는 경우
    elif(stack[-1] == seq[idx]):
        stack.pop()
        idx += 1
        logs.append('-')
    
    else:
        is_possible = False
        print('NO')
        break

if(is_possible):
    for s in logs:
        print(s)