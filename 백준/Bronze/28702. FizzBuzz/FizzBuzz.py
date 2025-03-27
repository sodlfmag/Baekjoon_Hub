'''
1. 3 5 6 9 10 12 15 18 20 ....
2. 1의 결과에서 연속된 세 개 문자열 중 적어도 하나는 숫자여야 함
3. isnumber를 통해 다음에 올 숫자를 계산 후 FizzBuzz 계산
'''
import sys
arr = sys.stdin.read().splitlines()
next = 0

for i in range(3):
    if(arr[i].isdigit()):
        next = int(arr[i]) + (3-i)
        break

if(next % 3 == 0):
    if(next % 5 == 0):
        print('FizzBuzz')
    else:
        print('Fizz')
elif(next % 5 == 0):
    print('Buzz')

else:
    print(next)
    