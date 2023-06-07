def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        temp = 0
        for j in range(len(photo[i])):
            if(photo[i][j] in name):
                index = name.index(photo[i][j])
                temp += yearning[index]
        
        answer.append(temp)
    return answer