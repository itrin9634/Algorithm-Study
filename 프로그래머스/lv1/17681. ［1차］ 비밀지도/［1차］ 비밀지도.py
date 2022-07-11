def solution(n, arr1, arr2):
    answer = []
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        arr1[i] = str(bin(arr1[i])[2:])
        arr1[i] = '0' * (n - len(arr1[i])) + arr1[i]
        arr2[i] = str(bin(arr2[i])[2:])
        arr2[i] = '0' * (n - len(arr2[i])) + arr2[i]
    for i in range(n):
        tmp = ''
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp) 
    
    return answer