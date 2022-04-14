from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])


bfs(graph, 0, 0)
print(graph[n-1][m-1])