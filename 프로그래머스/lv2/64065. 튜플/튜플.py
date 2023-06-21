'''
1. 각 튜플 내 요소를 분리해 2차원 리스트에 담기
2. 길이가 오름차순이 되도록 정렬 후 새로 생긴 값을 result 배열에 추가
'''


def solution(s):
    result = []
    s = s.lstrip('{')
    s = s.rstrip('}')
    arr = list(s.split('},{'))
    for i in range(len(arr)):
        arr[i] = list(map(int, arr[i].split(',')))
    
    arr.sort(key=lambda x:len(x))
    
    result.append(arr[0][0])
    
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j] not in result):
                result.append(arr[i][j])
                break
    return result