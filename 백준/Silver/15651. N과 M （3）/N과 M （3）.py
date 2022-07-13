n, m = map(int, input().split())
arr = [x for x in range(1, n+1)]
tmp = []


def sol():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return

    for i in arr:
        tmp.append(i)
        sol()
        tmp.pop()
    return


sol()