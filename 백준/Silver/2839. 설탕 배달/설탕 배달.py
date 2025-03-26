
n = int(input())

d = [0] * 5001
d[1] = -1
d[2] = -1
d[3] = 1
d[4] = -1
d[5] = 1

if(n > 5):
    for i in range(6, n+1):
        a = d[i-3]
        b = d[i-5]

        if(a > 0 and b > 0):
            d[i] = min(a, b) + 1
        elif(b == -1 and a > 0):
            d[i] = a + 1
        
        elif(a == -1 and b > 0):
            d[i] = b + 1
        else:
            d[i] = -1

print(d[n])