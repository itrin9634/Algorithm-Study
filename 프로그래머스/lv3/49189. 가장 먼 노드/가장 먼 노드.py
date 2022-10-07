from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)
    q = deque()
    q.append((1, 0))
    visited[1] = 0
    arr = []
    while q:
        now, cost = q.popleft()
        for i in graph[now]:
            if not visited[i] and i != 1:
                visited[i] = cost + 1
                q.append((i, cost+1))
    return visited.count(max(visited))