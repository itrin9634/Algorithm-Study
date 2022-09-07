import copy

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [0, 3], [1, 2], [2, 3]],
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    [[0, 1, 2, 3]]
]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def watch(x, y, mm, tmp):
    for i in mm:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny <0 or ny >= m or tmp[nx][ny] == 6:
                break
            elif tmp[nx][ny] == 0:
                tmp[nx][ny] = '#'


def dfs(n, arr):
    global ans
    tmp = copy.deepcopy(arr)

    #cctv 다 탐색 시
    if n == len(cctvs):
        count = 0
        for t in tmp:
            count += t.count(0)
        ans = min(ans, count)
        return

    x, y, k = cctvs[n]
    for d in mode[k]:
        watch(x, y, d, tmp)
        dfs(n+1, tmp)
        tmp = copy.deepcopy(arr)


cctvs = []
ans = int(1e9)

#cctv 위치 찾기
for i in range(n):
    for j in range(m):
        if 0 < arr[i][j] < 6:
            cctvs.append((i, j, arr[i][j]))

dfs(0, arr)
print(ans)