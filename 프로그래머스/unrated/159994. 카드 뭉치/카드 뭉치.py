'''
1. 원하는 순서 단어 배열 만들기
2. 카드를 순서대로 한 장씩 사용

1. 인덱스를 둘로 나눠서 다음 요소가 goal의 요소와 일치하는 지 비교함

'''

def solution(cards1, cards2, goal):
    s1 = 0
    s2 = 0
    for i in range(len(goal)):
        if(s1 < len(cards1)):
            if(cards1[s1] == goal[i]):
                s1 += 1
                continue
                
        if(s2 < len(cards2)):
            if(cards2[s2] == goal[i]):
                s2 += 1
                continue
        
        return("No")
    return("Yes")