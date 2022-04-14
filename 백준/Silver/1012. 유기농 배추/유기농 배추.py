from collections import deque

t = int(input())

#  상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y, visited, n, m):
    que = deque()
    que.append([x, y])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    que.append([nx, ny])
                    visited[nx][ny] = True


for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    answer = 0
    for b in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
    for p in range(n):
        for q in range(m):
            if not visited[p][q] and graph[p][q] == 1:
                bfs(graph, p, q, visited, n, m)
                answer += 1
    print(answer)
