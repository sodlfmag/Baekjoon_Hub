'''
1. 자카드 유사도 = 교집합 크기 / 합집합 크기
2. A B가 공집합인 경우는 1로 정의
3. 다중집합에도 가능
4. 문자열을 2개씩 끊어서 다중집합 처리하여 유사도를 계산
5. 둘다 영문인 경우만 쌍을 원소로 이용
6. 대소문자 구분 x

1. 입력된 문자열을 대문자화
2. 문자열을 두 개씩 끊어 배열에 담음
 -> 둘 다 알파벳이 아닌 경우는 제외
3. 각 딕셔너리에 개수를 저장
4. 각 배열을 set 화 한 뒤 교집합 연산 후 배열화 -> 교집합 원소 배열
5. 각 배열을 set 화 한 뒤 합집합 연산 후 배열화 -> 합집합 원소 배열
6. 교집합은 딕셔너리 min값 cnt
7. 합집합은 딕셔너리 max값 cnt
8. 둘 중 하나만 공집합이면 0
9. 둘 다 공집합이면 1
'''


def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    
    arr1 = []
    arr2 = []
    dic1 = {}
    dic2 = {}
    
    n_cnt = 0
    u_cnt = 0
    
    for i in range(len(str1) -1):
        temp = str1[i:i+2]
        if(temp.isalpha()):
            arr1.append(temp)
    for i in range(len(str2) -1):
        temp = str2[i:i+2]
        if(temp.isalpha()):
            arr2.append(temp)
    
    for i in range(len(arr1)):
        if(arr1[i] not in dic1):
            dic1[arr1[i]] = 1
        else:
            dic1[arr1[i]] += 1
    for i in range(len(arr2)):
        if(arr2[i] not in dic2):
            dic2[arr2[i]] = 1
        else:
            dic2[arr2[i]] += 1
            
    s1 = set(arr1)
    s2 = set(arr2)
    
    anb = list(s1 & s2)
    aub = list(s1 | s2)
    
    for i in range(len(anb)):
        n_cnt += min(dic1[anb[i]], dic2[anb[i]])
    
    for i in range(len(aub)):
        if(aub[i] in dic1 and aub[i] in dic2):
            u_cnt += max(dic1[aub[i]], dic2[aub[i]])
        
        elif(aub[i] in dic1):
            u_cnt += dic1[aub[i]]
        else:
            u_cnt += dic2[aub[i]]
    
    if(len(aub) == 0):
        return 65536
    else:
        return int((n_cnt / u_cnt) * 65536)