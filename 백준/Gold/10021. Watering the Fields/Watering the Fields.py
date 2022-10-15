import sys
import heapq
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


ans, cnt = 0, 0
n, c = map(int, input().split())
parent = [i for i in range(n)]
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

h = []
for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if dist >= c:
            heapq.heappush(h, (dist, i, j))

if len(h) < n - 1:
    print(-1)
else:
    while h:
        d, p1, p2 = heapq.heappop(h)
        if find_parent(parent, p1) != find_parent(parent, p2):
            union(parent, p1, p2)
            cnt += 1
            ans += d
            if cnt == n - 1:
                break
    if cnt == n - 1:
        print(ans)
    else:
        print(-1)

