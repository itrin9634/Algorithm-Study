n = int(input())

for i in range(n):
    string = input()
    stack1 = []
    stack2 = []
    for j in string:
        if j == '(':
            stack1.append(j)
        else:
            if len(stack1) > 0:
                stack1.pop()
            else:
                stack2.append(j)

    if len(stack1) == 0 and len(stack2) == 0:
        print("YES")
    else:
        print("NO")