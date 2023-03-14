def solution(n, m, section):
    answer = 0
    last = section[0] - 1
    for i in section:
        if last < i :
            last = i + m - 1
            answer += 1
    return answer