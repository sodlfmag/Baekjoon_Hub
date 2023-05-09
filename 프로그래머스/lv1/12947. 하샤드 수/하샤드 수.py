def solution(x):
    arr = list(map(int,str(x)))
    d = sum(arr)
    return x % d == 0