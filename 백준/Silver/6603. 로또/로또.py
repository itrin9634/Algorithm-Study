def dfs(tmp):
    if len(tmp) == 6:
        print(*tmp)
        return

    for i in range(len(s)):
        if s[i] not in tmp:
            if (tmp and tmp[-1] < s[i]) or not tmp:
                tmp.append(s[i])
                dfs(tmp)
                tmp.pop()


while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0:
        break
    s = arr[1:]
    tmp = []
    dfs(tmp)
    print()
