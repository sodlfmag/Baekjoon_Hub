'''
1. 딕셔너리에 상근이 카드를 입력
2. 2번째 카드 입력에서 in으로 value 출력
'''

n = int(input())
s = list(map(int, input().split()))

dic = dict()
for i in s:
    if(i in dic):
        dic[i] +=1
    else:
        dic[i] = 1

m = int(input())
arr = list(map(int, input().split()))

for i in arr:
    if(i in dic):
        print(dic[i], end=' ')
    else:
        print(0, end=' ')
