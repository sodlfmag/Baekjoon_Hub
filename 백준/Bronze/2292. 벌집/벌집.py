'''
1. 1 6 12 18 24 -> 1 제외 6씩 늘어나는 형태

2. 몫이 1 2 3 4 5.. 수열에서 몇번째에 해당하는지 구하기
3. 

'''

n = int(input())

cnt = 1

if(n == 1):
    print(1)
else:
    n -= 1
    while(True):
        if(1 <= n <= cnt * 6):
            cnt += 1
            break
        elif(n > cnt * 6):
            n -= cnt * 6
            cnt += 1
        else:
            break

    print(cnt)