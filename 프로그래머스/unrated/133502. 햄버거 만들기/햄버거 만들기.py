def solution(ingredient):
    answer = 0
    stack = []
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        if len(stack) >= 4:
            f4 = stack.pop()
            f3 = stack.pop()
            f2 = stack.pop()
            f1 = stack.pop()
            if f1 == 1 and f2 == 2 and f3 == 3 and f4 == 1:
                answer += 1
            else:
                stack.append(f1)
                stack.append(f2)
                stack.append(f3)
                stack.append(f4)
    return answer