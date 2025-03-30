'''
1. 각 키워드로 함수 만들기
2. n만큼 실행
3. split 으로 입력받아 배열 길이가 2인 경우만 push로 인식
'''

import sys
from collections import deque

def push(x):
    stack.append(x)

def pop():
    if(not stack):
        print(-1)
    else:
        print(stack.popleft())

def size():
    print(len(stack))

def empty():
    if(not stack):
        print(1)
    else:
        print(0)

def front():
    if(not stack):
        print(-1)
    else:
        print(stack[0])

def back():
    if(not stack):
        print(-1)
    else:
        print(stack[-1])


n = int(input())

stack = deque()

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
            
            case 'front':
                front()

            case 'back':
                back()