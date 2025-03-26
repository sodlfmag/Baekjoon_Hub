'''
1. 입력값 길이가 짝수면 반 나누고, 홀수면 중간 빼고 나눔
2. 한쪽을 반대로 바꾸고 == 연산
'''

import sys
while(True):
    s = sys.stdin.readline().strip()
    if(s == '0'):
        break
    
    if(len(s) == 1):
        print('yes')
    else:
        if(len(s) % 2 == 0):
            s1 = s[:len(s)//2]
            s2 = s[len(s)//2:]

            s2 = ''.join(list(reversed(s2)))
        
        else:
            s1 = s[:len(s)//2]
            s2 = s[len(s)//2 +1:]

            s2 = ''.join(list(reversed(s2)))

        if(s1 == s2):
            print('yes')
        else:
            print('no')
