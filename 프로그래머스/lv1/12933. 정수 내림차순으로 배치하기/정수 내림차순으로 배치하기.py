def solution(n):
    n = str(n)
    arr = list(n)
    arr.sort(reverse=True)
    return int(''.join(arr))