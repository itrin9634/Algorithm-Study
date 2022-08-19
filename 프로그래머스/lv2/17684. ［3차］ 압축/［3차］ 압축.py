dic = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def find(s):
    idx = 0
    n = 0
    while idx < len(s):
        idx += 1
        if s[:idx] in dic:
            n = idx
            continue
        else:
            break
    return s[:n], s[n:]


def solution(msg):
    answer = []
    global dic
    while msg:
        cur, msg = find(msg)
        next = ''
        if msg:
            next = msg[0]
            dic.append(cur+next)
        answer.append(dic.index(cur))
    return answer