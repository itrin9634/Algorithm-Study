n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
visited = [[False] * n for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0


def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    visited[x][y] = True
    if graph[x][y] == 1:
        cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)


houses = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            dfs(i, j)
            houses.append(cnt)
            cnt = 0
print(len(houses))
houses.sort()
for h in houses:
    print(h)