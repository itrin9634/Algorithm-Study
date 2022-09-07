def solution(survey, choices):
    answer = ''
    
    dic = {'R':0, 'T':0, 'C': 0, 'F':0, 'J': 0, 'M':0, 'A':0, 'N': 0}
    
    for i in range(len(survey)):
        a, b = survey[i]
        score = choices[i]
        if score - 4 < 0:
            dic[a] += abs(score - 4)
        else:
            dic[b] += abs(score - 4)
    arr = list(dic.items())
    for i in range(1, len(arr), 2):
        if arr[i-1][1] >= arr[i][1]:
            answer += arr[i-1][0]
        else:
            answer += arr[i][0]
    return answer