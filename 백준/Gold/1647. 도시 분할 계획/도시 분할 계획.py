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


max_cost = 0
result = 0

n, m = map(int, input().split())
parent = [0] * (n+1)
edges = []
for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)
        max_cost = max(max_cost, cost)

result -= max_cost
print(result)