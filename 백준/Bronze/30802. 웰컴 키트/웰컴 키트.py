import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

t, p = map(int, sys.stdin.readline().split())

cnt = 0
for i in range(6):
    if(arr[i] % t == 0):
        cnt += arr[i] // t
    else:
        cnt += arr[i] // t + 1

print(cnt)
print(n // p, n % p)