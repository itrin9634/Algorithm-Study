def solution(s):
    answer = True
    
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif stack:
            stack.pop()
        else:
            answer = False
            break
    if stack:
        answer = False

    return answer