'''
1. 캐시 크기에 따른 실행시간 측정 프로그램 만들기
2. LRU 알고리즘을 사용한다.
3. 실행시간 Hit - 1 , Miss - 5

1. LRU 방식이므로 queue를 사용해서 뒤로 밀어내는 방식을 쓴다.
2. Hit 하는 경우는 해당 값을 제일 뒤로 보내고 전부 왼쪽으로 민다.
3. Miss인 경우는 popleft 후 뒤에 해당 도시를 추가한다.
'''
from collections import deque
def solution(cacheSize, cities):
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    
    cnt = 0
    q = deque()
    if(cacheSize == 0):
        return 5 * len(cities)
    else:
        for i in range(len(cities)):
            # Hit
            if(cities[i] in q):
                temp = list(q)
                idx = temp.index(cities[i])
                q = deque(temp[:idx] + temp[idx+1:])
                q.append(temp[idx])
                cnt += 1
            # Miss
            else:
                # 덜 찬 경우
                if(len(q) < cacheSize):
                    q.append(cities[i])
                else:
                    q.popleft()
                    q.append(cities[i])
                cnt += 5
    return cnt