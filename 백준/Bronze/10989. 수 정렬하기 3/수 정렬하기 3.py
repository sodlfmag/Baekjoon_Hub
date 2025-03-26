import sys

n = int(sys.stdin.readline())  # 첫 번째 줄의 N 입력
result = [0] * 10001  # 10,000 이하의 자연수만 존재하므로 크기 10,001

# 입력값을 count 배열에 저장
for _ in range(n):
    num = int(sys.stdin.readline())
    result[num] += 1

# 정렬 없이 카운팅된 값만 출력
for i in range(10001):
    for _ in range(result[i]):
        print(i)