from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


#값 갱신해주는 함수
def set_graph(visit_array, val):
    for i in range(n):
        for j in range(n):
            if visit_array[i][j]:
                graph[i][j] = val


def bfs(x, y):
    q = deque()
    q.append((x, y))
    temp = []
    temp.append((x, y))

    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    temp.append((nx, ny))
    return temp

result = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                c = bfs(i, j)
                if len(c) > 1:
                    flag = True
                    number = sum([graph[x][y] for x, y in c]) // len(c)
                    for x, y in c:
                        graph[x][y] = number
    if not flag:
        break
    result += 1
print(result)