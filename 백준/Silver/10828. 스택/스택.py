'''
1. 각 키워드로 함수 만들기
2. n만큼 실행
3. split 으로 입력받아 배열 길이가 2인 경우만 push로 인식
'''

import sys

def push(x):
    stack.append(x)

def pop():
    if(not stack):
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if(not stack):
        print(1)
    else:
        print(0)

def top():
    if(not stack):
        print(-1)
    else:
        print(stack[-1])


n = int(input())

stack = []

for i in range(n):
    command = list(sys.stdin.readline().split())
    if(len(command) == 2):
        push(command[1])
    else:
        match command[0]:
            case 'pop':
                pop()
            
            case 'size':
                size()
            
            case 'empty':
                empty()
            
            case 'top':
                top()


