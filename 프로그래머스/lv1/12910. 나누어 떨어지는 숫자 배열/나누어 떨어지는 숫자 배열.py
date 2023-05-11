def solution(arr, divisor):
    answer = []
    for ele in arr:
        if(ele % divisor == 0):
            answer.append(ele)
    answer.sort()
    if(len(answer) == 0):
        return [-1]
    return answer