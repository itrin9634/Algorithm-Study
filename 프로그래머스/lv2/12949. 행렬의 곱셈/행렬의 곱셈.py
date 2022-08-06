def solution(arr1, arr2):
    n, m = len(arr1), len(arr1[0])
    N, M = len(arr2), len(arr2[0])
    answer = []
    for i in range(n):
        temp = []
        for j in range(M):
            tmp = 0
            for k in range(m):
                tmp += (arr1[i][k] * arr2[k][j])
            temp.append(tmp)
            tmp = 0
        answer.append(temp)
        temp = []       
            
    return answer