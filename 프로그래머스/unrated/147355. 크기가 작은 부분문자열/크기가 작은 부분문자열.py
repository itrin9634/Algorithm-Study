def solution(t, p):
    answer = 0
    length = len(p)
    for i in range(len(t) - len(p) + 1):
        if int(t[i:length + i]) <= int(p):
            answer += 1
    return answer