n = int(input())
s = input()  # 후위 표기식
al_val = []
stack = []
for i in range(n):
    al_val.append(int(input()))
for i in s:
    if i.isalpha():
        stack.append(al_val[(ord(i)-65)])
    else:
        op2 = stack.pop()
        op1 = stack.pop()
        if i == "*":
            stack.append(op1 * op2)
        elif i == "+":
            stack.append(op1 + op2)
        elif i == "-":
            stack.append(op1 - op2)
        elif i == "/":
            stack.append(op1 / op2)
if stack:
    print("%.2f" % (stack.pop()))

