from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)] 

for _ in range(m):
    b, a = map(int, input().split())
    arr[a].append(b)


def bfs(start):
    q = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    cnt = 1
    while q:
        now = q.popleft()
        for i in arr[now]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                q.append(i)
    return cnt

results = []
max_cnt = 0
for i in range(1, n+1):
    tmp_cnt = bfs(i)
    if tmp_cnt > max_cnt:
        max_cnt = tmp_cnt
    results.append([i, tmp_cnt])

for k, cnt in results:
    if cnt == max_cnt:
        print(k, end = ' ')