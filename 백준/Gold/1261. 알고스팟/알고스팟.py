from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


q = deque()
q.append((0, 0))
dist[0][0] = 0

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
            if arr[nx][ny] == 0:
                dist[nx][ny] = dist[x][y]
                q.appendleft((nx, ny))
            else:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


print(dist[n-1][m-1])