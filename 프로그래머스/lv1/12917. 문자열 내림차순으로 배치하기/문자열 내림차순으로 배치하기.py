def solution(s):
    arr = list(s)
    arr.sort(reverse=True)
    result = ''.join(arr)
    return result