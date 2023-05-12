def solution(s, n):
    arr = list(s)
    for i in range(len(arr)):
        if not (arr[i].isalpha()):
            continue
        temp = ord(arr[i]) + n
        if(arr[i].isupper()):
            if(temp > ord('Z')):
                temp -= 26
        else:
            if(temp > ord('z')):
                temp -= 26
        arr[i] = chr(temp)
    result = ''.join(arr)
    return result