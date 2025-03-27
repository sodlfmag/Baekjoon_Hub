'''
1. 666을 하나의 청크로 본다.
2. 앞에 숫자가 붙고 -> 뒤에 숫자가 붙는 순서 
3. 무지성 조합 만들고 정렬
'''
n = int(input())
arr = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                arr.append(int('666' + str(i) + str(j) + str(k) + str(l)))
                arr.append(int(str(i) + '666' + str(j) + str(k) + str(l)))
                arr.append(int(str(i) + str(j) + '666' + str(k) + str(l)))
                arr.append(int(str(i) + str(j) + str(k) + '666' + str(l)))
                arr.append(int(str(i) + str(j) + str(k) + str(l) + '666'))
arr = list(set(arr))
arr.sort()
print(arr[n-1])