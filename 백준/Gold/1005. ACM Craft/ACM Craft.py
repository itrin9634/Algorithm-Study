from collections import deque

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    times = [0]+ list(map(int, input().split())) # 건물당 건설에 걸리는 시간
    indegree = [0] * (n+1)
    dp = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for j in range(k):
        x, y = map(int, input().split())
        indegree[y] += 1
        graph[x].append(y)
    w = int(input())
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = times[i]
    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + times[i])
            if indegree[i] == 0:
                q.append(i)
    print(dp[w])