n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)
cnt = 0
for i in range(2, n+1):
    if visited[i]:
        cnt += 1
print(cnt)
