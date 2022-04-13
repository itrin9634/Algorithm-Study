from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

#상하좌우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y, h):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > h:
                    q.append([nx, ny])
                    visited[nx][ny] = True


max_h = max(map(max, graph))
result = 0
for h in range(max_h):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                cnt += 1
                bfs(i, j, h)
    result = max(result, cnt)
print(result)

