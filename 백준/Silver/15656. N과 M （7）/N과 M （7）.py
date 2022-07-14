n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []


def sol():
    if len(tmp) == m:
        print(*tmp)
        return
    for i in arr:
        tmp.append(i)
        sol()
        tmp.pop()


sol()