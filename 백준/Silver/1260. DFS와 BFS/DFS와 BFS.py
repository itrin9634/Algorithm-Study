from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        print(x, end = ' ')
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)