'''
1. n개의 개인정보
2. 각 개인정보는 유효기간이 지나면 파기
3. 모든 달은 28일까지 있다고 가정
4. 기한은 정수로 달 수로 정함
5. 파기해야 할 개인정보를 오름차순으로 배열 정렬 반환

1. terms를 split 하여 딕셔너리에 숫자값으로 저장
2. privacies 요소를 split하여 유효기간 산정
3. today와 비교하여 날짜가 작은 정보를 result에 반환 - 첫번째 요소가 1번

'''
import math
def solution(today, terms, privacies):
    dic = {}
    answer = []
    dates = []
    today = list(map(int, today.split('.')))
    for i in range(len(terms)):
        clas, term = terms[i].split()
        term = int(term)
        dic[clas] = term
    print(dic)
    
    for i in range(len(privacies)):
        date, clas = privacies[i].split()
        dates.append(list(map(int, date.split('.'))))
        dates[i].append(clas)
        
    for i in range(len(privacies)):
        term = dic[dates[i][3]]
        dates[i][1] += term
        
        if(13 <= dates[i][1]):
            unit = dates[i][1] / 12
            if(unit % 1 == 0 ):
                unit -= 1
            else:
                unit = math.floor(unit)
            
            dates[i][0] += unit
            dates[i][1] -= 12 * unit

    
    for i in range(len(dates)):
        # 연단위 초과
        if(today[0] > dates[i][0]):
            answer.append(i+1)
            continue
        # 월단위 초과
        elif(today[0] == dates[i][0] and today[1] > dates[i][1]):
            answer.append(i+1)
            continue
        # 일단위 초과
        elif(today[0] == dates[i][0] and today[1] == dates[i][1] and today[2] >= dates[i][2]):
            answer.append(i+1)
            continue

    return answer