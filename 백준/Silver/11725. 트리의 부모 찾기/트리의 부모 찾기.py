import sys
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)

ans = [0] * (n+1)
while q:
    now = q.popleft()
    for i in graph[now]:
        if ans[i] == 0:
            ans[i] = now
            q.append(i)

for i in range(2, n+1):
    print(ans[i])