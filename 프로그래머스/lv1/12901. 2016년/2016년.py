import datetime as dt

def solution(a, b):
    days = ["SUN","MON","TUE","WED","THU","FRI",'SAT']
    dt1 = dt.datetime(2016,1,1)
    dt2 = dt.datetime(2016,a,b)
    td = dt2 - dt1
    td = td.days % 7
    index = (5 + td) % 7
    answer = days[index]
    return answer