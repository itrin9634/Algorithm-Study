def solution(X, Y):
    answer = ''
    arr = sorted(list(set(X) & set(Y)), reverse = True)
    for i in arr:
        answer += i * min(X.count(i), Y.count(i))
    if answer:
        if answer[0] == '0':
            return '0'
        else:
            return answer
    else:
        return '-1'