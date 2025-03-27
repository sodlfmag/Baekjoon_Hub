import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

arr = list(set(arr))
arr.sort()

for i in range(len(arr)):
    print(arr[i])
