import sys
a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline().rstrip())
n0 = int(sys.stdin.readline().rstrip())

def f(a0,a1,n):
    return a1 * n + a0

def g(c, n):
    return c * n

flag = True
if(f(a0,a1,n0) <= g(c, n0)):
    if(a1 <= c):
        flag = True
    else:
        flag = False
        
else:
    flag = False

if(flag):
    print(1)
else:
    print(0)