'''
1. 스택에 '(' 쌓기
2. ')' 입력 들어오면 pop해서 비교
'''
import sys

stack = []
n = int(input())

for i in range(n):
    stack = []
    input = sys.stdin.readline().rstrip()
    
    is_vps = True
    for s in input:
        if(s == '('):
            stack.append('(')
        elif(s == ')'):
            if(len(stack) == 0 or stack.pop() != '('):
                is_vps = False
                break
        
    if(is_vps and len(stack) == 0):
        print('YES')
    else:
        print('NO')
           