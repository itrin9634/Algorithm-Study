n, m, h = map(int, input().split())
arr = [[False] * n for _ in range(h)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = True
ans = int(1e9)


# 사다리 확인
def check():
    for start in range(n):
        k = start
        for j in range(h):
            if arr[j][k]:
                k += 1
            elif k > 0 and arr[j][k-1]:
                k -= 1
        if k != start:
            return False
    return True


# 사다리 추가
def dfs(cnt, x, y):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return

    for i in range(x, h):
        k = y if i == x else 0
        for j in range(k, n-1):
            if not arr[i][j]:
                arr[i][j] = True
                dfs(cnt+1, i, j + 2)
                arr[i][j] = False


dfs(0, 0, 0)
if ans <= 3:
    print(ans)
else:
    print(-1)