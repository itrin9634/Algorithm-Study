from collections import deque
MAX = 100001
visited = [False] * MAX
n, k = map(int, input().split())
q = deque()
time = 0
q.append((n, time))

while q:
    now, time = q.popleft()
    visited[now] = True
    if now == k:
        print(time)
        break

    if 0 <= now * 2 < MAX and not visited[now * 2]:
        q.append((now * 2, time))
        
    if 0 <= now - 1 < MAX and not visited[now-1]:
        q.append((now - 1, time + 1))
    if 0 <= now +1 < MAX and not visited[now + 1]:
        q.append((now + 1, time + 1))
