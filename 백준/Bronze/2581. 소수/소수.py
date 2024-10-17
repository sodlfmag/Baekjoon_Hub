import sys, math
m, n = map(int, sys.stdin.read().splitlines())
result = []
for i in range(m, n+1):
    if i < 2:
        continue
    flag = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if(i % j == 0):
            flag = False
            break
    if(flag):
        result.append(i)

if(result):
    print(sum(result))
    print(min(result))
else:
    print(-1)