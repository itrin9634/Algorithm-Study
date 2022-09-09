def solution(s):
    answer = True
    
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            answer = False
            break
    if cnt:
        answer = False

    return answer