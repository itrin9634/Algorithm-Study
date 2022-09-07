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
            
    if dic['R'] >= dic['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dic['C'] >= dic['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dic['J'] >= dic['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dic['A'] >= dic['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer