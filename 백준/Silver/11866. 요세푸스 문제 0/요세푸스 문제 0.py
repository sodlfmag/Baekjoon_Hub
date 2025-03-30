'''
1. k번 돌아가면서 인덱스 == len(arr)인 경우 0으로 돌림
2. 삭제되면 현재 인덱스는 그대로 유지 -> 끝 인덱스가 삭제된 경우 -1 예외처리
3. delete()로 수행 - 50만번 연산 -> 브루트포스
'''


n, k = map(int, input().split())

arr = list(map(str, range(1, n+1)))
result = []
idx = 0

while arr:
    idx = (idx + k-1) % len(arr)
    result.append(arr[idx])
    del arr[idx]
    if(idx == len(arr)):
       idx = 0

s = ', '.join(result)
print('<' + f'{s}' + '>')
