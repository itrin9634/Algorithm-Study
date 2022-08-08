from collections import deque


def bfs(start, graph):
    q = deque()
    q.append((start, 0, str(start)))
    graph[start] = True

    while q:
        now, time, result = q.popleft()
        if now == k:
            print(time)
            print(result)
            return

        if 0 <= now + 1 < MAX and not graph[now + 1]:
            graph[now + 1] = True
            q.append((now + 1, time + 1, result + ' ' + str(now + 1)))
        if 0 <= now - 1 < MAX and not graph[now - 1]:
            graph[now - 1] = True
            q.append((now - 1, time + 1, result + ' ' + str(now - 1)))
        if 0 <= now * 2 < MAX and not graph[now * 2]:
            graph[now * 2] = True
            q.append((now * 2, time + 1, result + ' ' + str(now * 2)))


n, k = map(int, input().split())
MAX = 100001
visited = [False] * MAX
bfs(n, visited)
