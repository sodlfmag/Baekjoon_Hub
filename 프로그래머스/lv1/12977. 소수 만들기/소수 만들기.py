def solution(nums):
    cnt = 0

    arr = []
    
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                arr.append(nums[i]+nums[j]+nums[k])
    
    s = arr[:]
    for i in range(len(s)):
        isPrime = True
        if(s[i] == 3):
            cnt += 1
            continue
        for j in range(2, s[i]//2 +1):
            if((s[i] / j) % 1 == 0 ):
                isPrime = False
                break
        if(isPrime):
            cnt+=1
    
    return cnt