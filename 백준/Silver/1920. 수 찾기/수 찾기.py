'''
1. 딕셔너리에 키 저장
2. in 연산으로 있으면 1 없으면 0 출력
'''

n = int(input())
input_a = list(map(int, input().split()))

dic = dict()

for i in input_a:
    dic[i] = 1


m = int(input())
input_b = list(map(int, input().split()))

for i in input_b:
    if(i in dic):
        print(1)
    else:
        print(0)
