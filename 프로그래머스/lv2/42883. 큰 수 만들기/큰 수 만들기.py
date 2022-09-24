def solution(number, k):
    answer = ''
    stack = [number[0]]
    
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0 :
            k -= 1
            stack.pop()
        stack.append(num)
    if k:
        stack = stack[:-k]
        
    return ''.join(stack)