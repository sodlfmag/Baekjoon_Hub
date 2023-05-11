def solution(price, money, count):
    total_price = ((count + 1) * price ) * (count / 2)
    answer = total_price - money
    if(answer <= 0):
        return 0
    return answer