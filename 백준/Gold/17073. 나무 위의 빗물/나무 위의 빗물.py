from collections import deque

n, w = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
leaf = 0

q = deque()
q.append(1)
while q:
    now = q.popleft()
    visited[now] = True
    isParent = False
    for i in graph[now]:
        if not visited[i]:
            isParent = True
            q.append(i)
            visited[i] = True
    if not isParent:
        leaf += 1
print(w / leaf)
