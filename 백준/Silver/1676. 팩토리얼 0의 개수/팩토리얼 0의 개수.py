def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = int(input())
s = list(str(factorial(n)))
s.reverse()

cnt = 0

for i in range(len(s)):
    if(s[i] == '0'):
        cnt += 1
    else:
        break

print(cnt)