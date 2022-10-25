def solution(a, b, n):
    answer = 0
    while n >= a:
        mod = n % a
        n = (n // a) * b
        answer += n
        n += mod
    return answer