import itertools
n, m = map(int, input().split())
arr = [x for x in range(1, n+1)]
tmp = []


def sol(start):
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))

        return
    for i in range(start, n+1):
        if i not in tmp:
            tmp.append(i)
            sol(i+1)
            tmp.pop()
    return


sol(1)
