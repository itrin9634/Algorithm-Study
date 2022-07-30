def dfs(tmp, idx, total):
    global result
    if len(tmp) > 0 and total == s:
        result += 1
    for i in range(idx+1, len(arr)):
        tmp.append(arr[i])
        total += arr[i]
        dfs(tmp, i, total)
        total -= tmp.pop()


n, s = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
tmp = []
dfs(tmp, -1, 0)
print(result)