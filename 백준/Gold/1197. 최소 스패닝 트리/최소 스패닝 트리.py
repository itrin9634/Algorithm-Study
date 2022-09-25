v, e = map(int, input().split())
parent = [i for i in range(v+1)]
dist = []
for i in range(e):
    a, b, c = map(int, input().split())
    dist.append((c, a, b))
dist.sort()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


ans = 0
for d in dist:
    cost, a, b = d
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += cost
print(ans)