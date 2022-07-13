n, m = map(int, input().split())
tmp = []


def sol(start):
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return

    for i in range(start, n+1):
        tmp.append(i)
        sol(i)
        tmp.pop()
    return


sol(1)