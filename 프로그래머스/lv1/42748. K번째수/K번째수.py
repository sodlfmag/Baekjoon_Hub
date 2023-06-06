def solution(array, commands):
    result = []
    for t in range(len(commands)):
        i = commands[t][0]
        j = commands[t][1]
        k = commands[t][2]
        
        temp = array[i-1:j]
        temp.sort()
        val = temp[k-1]
        
        result.append(val)
        
    return result