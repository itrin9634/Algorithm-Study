n = int(input())
parent = [i for i in range(n)]


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

ans = 0
arr = [list(map(int, input().split())) for _ in range(n)]
dists = []

for i in range(n):
    for j in range(n):
        dists.append((arr[i][j], i, j))
dists.sort()

for i in range(len(dists)):
    cost, a, b = dists[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        ans += cost
print(ans)