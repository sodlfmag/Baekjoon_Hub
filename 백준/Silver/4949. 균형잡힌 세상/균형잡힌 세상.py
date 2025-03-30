'''
1. 스택에 괄호 쌓기
2. ')', ')'가 입력으로 들어오면 스택 pop 후 비교해서 다르면 no 출력
3. .을 만(을 때 스택이 비어있으면 yes
'''

import sys
while(True):
    input = sys.stdin.readline().rstrip()
    input = input[:-1]
    
    # 종료조건
    if(input == ''):
        break

    stack = []

    is_balanced = True
    for s in input:
        if(s == '[' or s == '('):
            stack.append(s)
        
        elif(s == ']'):
            if(len(stack) == 0 or stack.pop() != '['):
                is_balanced =False
                break
        
        elif(s == ')'):
            if(len(stack) == 0 or stack.pop() != '('):
                is_balanced =False
                break
    
    if(is_balanced and len(stack) == 0):
        print('yes')
    else:
        print('no')
        
