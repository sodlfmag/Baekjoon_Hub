n = int(input())
flag = True
if(n != 1):
    while flag:
        for i in range(2,n+1):
            if(n % i == 0):
                print(i)
                if(n == i):
                    flag = False
                    break
                
                n = n // i
                break