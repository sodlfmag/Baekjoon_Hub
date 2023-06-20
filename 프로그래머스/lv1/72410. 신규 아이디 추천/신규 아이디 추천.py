'''
1. 규칙 위반 아이디 입력 시, 유사하면서 규칙 준수한 아이디 추천
2. 소문자, '-', '_', '.' 만 사용 가능
3. '.'는 처음과 끝 사용 불가
4. '.'는 연속사용 불가


'''

def solution(new_id):
    symbols = ['-', '_', '.']
    
    # 1단계 - 소문자 치환
    new_id = new_id.lower()
    # 2단계 - 기호 제거
    arr = list(new_id)
    for i in range(len(arr)):
        if(not arr[i].isalpha() and not arr[i].isdigit() and arr[i] not in symbols):
            arr[i] = ''
    new_id = ''.join(arr)    
    
    # 3단계 - 마침표 중복 1개로 줄이기
    arr = list(new_id)
    for i in range(len(arr) -1):
        if(arr[i] == '.'):
            if(arr[i+1] == '.'):
                arr[i] = ''
    new_id = ''.join(arr)            
    
    # 4단계 - 처음과 끝 마침표 제거
    arr = list(new_id)
    if(len(arr) > 0):
        if(arr[0] == '.'):
            arr[0] = ''
    if(len(arr) > 0):
        if(arr[-1] == '.'):
            arr[-1] = ''
    new_id = ''.join(arr)
    # 5단계 - 빈 문자열이면 "a" 추가
    if(len(new_id) == 0):
        new_id = 'a'
    # 6단계 - 16자 이상일 시 첫 15개만 남김
            #-> 4단계 다시 진행
    if(len(new_id) >= 16):
        new_id = new_id[:15]
    
    arr = list(new_id)
    if(len(arr) > 0):
        if(arr[0] == '.'):
            arr[0] = ''
    if(len(arr) > 0):
        if(arr[-1] == '.'):
            arr[-1] = ''
    new_id = ''.join(arr)
    
    # 7단계 - 길이가 2자 이하면 마지막 문자를 길이가 3이 될 때까지 끝에 붙임
    if(len(new_id) <= 2):
        temp = new_id[-1]
        new_id += temp * (3-len(new_id))
    return new_id