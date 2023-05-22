def solution(n, arr1, arr2):
    temp1 = []
    temp2 = []
    graph = []
    for i in range(n):
        temp = list(map(int, bin(arr1[i])[2:].zfill(n)))
        temp1.append(temp)
        
    for i in range(n):
        temp = list(map(int,bin(arr2[i])[2:].zfill(n)))
        temp2.append(temp)  
    
    for i in range(n):
        graph.append([])
        for j in range(n):
            if(temp1[i][j] or temp2[i][j]):
                graph[i].append('#')
            else:
                graph[i].append(' ')
    
    for i in range(n):
        temp = ''.join(graph[i])
        graph[i] = temp
        
    return graph