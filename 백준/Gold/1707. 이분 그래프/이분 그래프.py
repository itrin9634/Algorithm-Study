from collections import deque


def bfs(start, group):
    q = deque()
    q.append(start)
    global error
    visited[start] = group

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = -(visited[now])
                q.append(i)
            elif visited[i] == visited[now]:
                error = True
                return


t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    error = False

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        if not visited[i]:
            bfs(i, 1)
        if error:
            break
    if error:
        print('NO')
    else:
        print('YES')