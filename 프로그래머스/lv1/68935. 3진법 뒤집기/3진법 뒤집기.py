def sol(n, q):
    s = []
    while n > 0:
        k, m = divmod(n, q)
        s.append(m)
        n = k
    s = ''.join(map(str, s))
    s = int(s, 3)
    return s


def solution(n):
    answer = sol(n, 3)
    return answer