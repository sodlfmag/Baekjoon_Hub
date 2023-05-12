def solution(s):
    temp = list(s.split(' '))
    print(temp)
    arr = []
    for val in temp:
        arr.append(list(val))
        
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(j % 2 == 0):
                arr[i][j] = arr[i][j].upper()
            else:
                arr[i][j] = arr[i][j].lower()
    
    arr2 = []
    
    for i in range(len(arr)):
        arr2.append(''.join(arr[i]))
    print(arr2)
    
    return ' '.join(arr2)
    
                