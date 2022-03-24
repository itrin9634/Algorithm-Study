s = input()  # 중위 표기식
op = []
result = ""
tag = 0


def op_rank(k):
    if k == "(":
        return 0
    elif k == "+" or k == "-":
        return 1
    elif k == "*" or k == "/":
        return 2


for i in s:
    if i.isalpha():
        result += i
    else:
        if i == "(":
            op.append(i)
        elif i == ")":
            while op[-1] != "(":
                result += op.pop()
            op.pop()
        else:
            while op and op_rank(op[-1]) >= op_rank(i):
                result += op.pop()
            op.append(i)    


while op:
    result += op.pop()

print(result)
