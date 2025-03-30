import sys, math

n = int(input())
dic = dict()
arr = [0] * n
for i in range(n):
    temp = int(sys.stdin.readline().rstrip())
    arr[i] = temp
    if(temp in dic):
        dic[temp] += 1
    else:
        dic[temp] = 1 

arr.sort()

# 1. 산술평균
total = sum(arr)
if(total > 0):
    print(math.floor((total / n) + 0.5))
else:
    print(math.ceil((total /n)-0.5))

# 2. 중앙값
print(arr[n//2])

# 3. 최빈값
freq = list(dic.items())
freq.sort(key=lambda x:(-x[1], x[0]))
ma = freq[0][1]

temp = []
for i in range(len(freq)):
    if(freq[i][1] == ma):
        temp.append(freq[i][0])
    else:
        break

if(len(temp)==1):
    print(temp[0])
else:
    print(temp[1])

#4. 범위
print(arr[-1] - arr[0])

