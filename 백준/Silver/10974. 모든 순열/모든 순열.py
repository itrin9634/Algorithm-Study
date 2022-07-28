tmp = []
n = int(input())
arr = [i for i in range(1, n+1)]


def dfs():
    if len(tmp) == n:
        print(*tmp)
        return
    for a in arr:
        if a not in tmp:
            tmp.append(a)
            dfs()
            tmp.pop()


dfs()