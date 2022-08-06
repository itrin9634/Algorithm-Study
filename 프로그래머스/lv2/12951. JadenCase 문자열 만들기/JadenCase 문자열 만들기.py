def solution(s):
    s = s.lower()
    idx = 0
    answer = ''
    for i in range(len(s)):
        if idx == 0 and s[i].isalpha():
            answer += s[i].upper()
            idx += 1
            continue
        elif s[i] == ' ':
            idx = 0
        else:
            idx += 1
        answer += s[i]

    return answer
