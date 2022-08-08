from collections import deque

#이동 가능 방향
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]


def bfs(graph):
    cnt = 0
    q = deque()
    q.append((start_x, start_y, cnt))
    graph[start_x][start_y] = 1 #방문 표시

    while q:
        now_x, now_y, cnt = q.popleft()
        if now_x == goal_x and now_y == goal_y:
            print(cnt)
            return

        for i in range(8):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph) and not graph[nx][ny]:
                q.append((nx, ny, cnt + 1))
                graph[nx][ny] = 1


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    start_x, start_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    bfs(arr)