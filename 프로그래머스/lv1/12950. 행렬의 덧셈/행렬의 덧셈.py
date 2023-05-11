def solution(arr1, arr2):
    matrix = []
    for i in range(len(arr1)):
        matrix.append([])
        for j in range(len(arr1[i])):
            matrix[i].append(arr1[i][j] + arr2[i][j])
    return matrix