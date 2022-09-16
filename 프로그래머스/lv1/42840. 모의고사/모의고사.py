def solution(answers):
    answer = []
    hash = dict()
    arr = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5,], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(3):
        cnt = 0
        for j in range(len(answers)):
            if answers[j] == arr[i][j % len(arr[i])]:
                cnt += 1
        hash[i+1] = cnt
    MAX = max(hash.values())
    for (i, v) in hash.items():
        if v == MAX:
            answer.append(i)
        
    return answer