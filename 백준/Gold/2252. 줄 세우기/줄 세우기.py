from collections import deque
n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    print(cur, end = ' ')
    for i in graph[cur]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

