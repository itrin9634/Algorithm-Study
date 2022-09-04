def solution(n):
    ans = 0
    while n > 1:
        if n % 2 != 0:
            ans += 1
        n //= 2
    if n == 1:
        ans += 1
    return ans