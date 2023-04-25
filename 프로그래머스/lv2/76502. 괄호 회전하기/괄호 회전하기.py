def findOp(s):
    if s == ']':
        return '['
    if s == ')':
        return '('
    if s == '}':
        return '{'


def isRight(s):
    stack = []
    for i in range(len(s)):
        stack1 = []
        if s[i] in (']', ')', '}'):
            find = False
            val = 0
            op = findOp(s[i])
            while stack:
                tmp = stack.pop()
                if tmp == op:
                    find = True
                    break
                if tmp in (']', ')', '}'):
                    val -= 1
                else:
                    val += 1
                stack1.append(tmp)
            if not find or val:
                return False
            stack += stack1
        else:
            stack.append(s[i])
    if stack:
        return False
    return True
def solution(s):
    cnt = 0
    for i in range(len(s)):
        new_s = s[i:] + s[:i]
        if isRight(new_s):
            cnt += 1
    return cnt