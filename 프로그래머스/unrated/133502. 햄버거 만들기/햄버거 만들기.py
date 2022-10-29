def solution(ingredient):
    answer = 0
    stack = []
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
    return answer