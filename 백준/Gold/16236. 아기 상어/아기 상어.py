from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
now_x, now_y = 0, 0
size = 2
ate = 0
result = 0
INF = int(1e9)

#상좌하우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            now_x, now_y = i, j
            arr[now_x][now_y] = 0


def bfs():
    q = deque()
    dist = [[-1] * n for _ in range(n)]
    q.append([now_x, now_y])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1 and arr[nx][ny] <= size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


def find(dist):
    min_dist = INF
    x, y = 0, 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= arr[i][j] < size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist


while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    now_x, now_y = value[0], value[1]
    result += value[2]
    arr[now_x][now_y] = 0
    ate += 1
    if ate >= size:
        size += 1
        ate = 0
