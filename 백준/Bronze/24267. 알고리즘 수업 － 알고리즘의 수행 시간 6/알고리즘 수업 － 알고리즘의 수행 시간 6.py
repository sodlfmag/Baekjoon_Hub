import sys
n = int(sys.stdin.readline().rstrip())
total = 0
for i in range(1, n-1):
    total += (i * (i+1)) // 2
print(total)
print(3)
