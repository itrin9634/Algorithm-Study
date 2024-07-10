def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs:
        tmp = str[s:s+l]
        if int(tmp) > k:
            answer.append(int(tmp))
    return answer
