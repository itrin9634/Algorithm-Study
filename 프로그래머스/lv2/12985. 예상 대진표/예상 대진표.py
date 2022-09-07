def is_meet(n, a, b):
    meet = False
    if 0 < a <= n and 0 < b <= n and b - a == 1:
        if a % 2 == 1 and b % 2 == 0:
            meet = True
    return meet


def solution(n,a,b):
    answer = 0
    if a > b:
        a, b = b, a
    
    while n > 1:
        answer += 1
        if is_meet(n, a, b):
            break
        a = (a + 1) // 2
        b = (b + 1) // 2
        n //= 2

    return answer