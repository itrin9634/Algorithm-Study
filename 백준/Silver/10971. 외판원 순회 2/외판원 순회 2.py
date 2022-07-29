def dfs(arr, start, now, total):
    global min_val
    if len(arr) == n:
        if w[now][start] != 0:
            total += w[now][start]
            min_val = min(min_val, total)
        return

    for i in range(n):
        if i not in arr and w[now][i] != 0:
            arr.append(i)
            dfs(arr, start, i, total + w[now][i])
            arr.pop()


n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
arr = []
min_val = int(1e9)

for i in range(n):
    if i not in arr:
        arr.append(i)
        dfs(arr, i, i, 0)
        arr.pop()

print(min_val)