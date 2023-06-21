'''
1. 한 번에 한 명 신고 가능
2. 신고 횟수 제한 x
3. 중복 신고는 1회 처리
4. k번 이상 신고된 유저는 정지
5. 정지된 유저를 신고한 유저한테 메일을 보냄
6. 정지 처리 메일을 받는 횟수를 배열로 반환

1. 각 유저이름을 key, 집합을 값으로 갖는 딕셔너리에 report 요소 split하여 추가 - 중복처리
2. 신고 횟수를 카운트하는 딕셔너리를 만들어 딕셔너리 1의 values를 전부 꺼내 카운트 해줌
3. 카운트 사전에서 값이 k를 넘는 key만 배열로 뺌
4. report 사전에서 유저 당 밸류 in values로 연산값 추가
'''

def solution(id_list, report, k):
    dic_r = {}
    dic_c = {}
    wanted = []
    result = [0] * len(id_list)
    
    for i in range(len(id_list)):
        dic_r[id_list[i]] = set()
        dic_c[id_list[i]] = 0
    
    for i in range(len(report)):
        rep, send = report[i].split()
        dic_r[rep].add(send)
    
    for i in range(len(id_list)):
        temp = list(dic_r[id_list[i]])
        for j in range(len(temp)):
            dic_c[temp[j]] += 1
    total = list(dic_c.values())
    
    for i in range(len(total)):
        if(total[i] >= k):
            wanted.append(id_list[i])
            
    for i in range(len(id_list)):
        for j in range(len(dic_r[id_list[i]])):
            if(list(dic_r[id_list[i]])[j] in wanted):
                result[i] += 1
    
    return result