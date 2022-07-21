#균형잡힌 괄호 문자열로 분리
def separate(sen):
    cnt = 0
    for i in range(len(sen)):
        if sen[i] == '(':
            cnt += 1
        elif sen[i] == ')':
            cnt -= 1
        if cnt == 0:
            return sen[:i+1], sen[i+1:]

# 올바른 괄호 문자열 판단
def right_string(sen):
    cnt = 0
    
    for i in sen:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True

#첫번째, 마지막 문자 제거 후 나머지 문자열 괄호 방향 뒤집기
def reverse(sen):
    result = ''
    sen = list(sen[1:-1])
    for i in range(len(sen)):
        if sen[i] == '(':
            result += ')'
        else:
            result += '('
    return result

def solution(p):
    answer = ''
    # 빈 문자열인 경우
    if not p:
        return answer
    
    u, v = separate(p)
    if right_string(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')' + reverse(u)
    return answer
    