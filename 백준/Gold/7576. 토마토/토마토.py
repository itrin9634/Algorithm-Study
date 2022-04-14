from collections import deque
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))
while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
answer = True
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer = False
            break

if answer:
    print(max(map(max, graph)) - 1)
else:
    print(-1)
