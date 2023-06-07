def solution(a, b, n):
    left = n
    coke = 0
    rest = 0
    while(left >= a):
        coke += (left // a) * b
        rest = left % a
        left = (left // a) *b + rest
        
        # print( coke, rest, left)

    return coke