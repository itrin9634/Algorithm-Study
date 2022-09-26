n = int(input())
m = int(input())

graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))
graph.sort()
parent = [i for i in range(n+1)]


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
for i in range(len(graph)):
    cost, x, y = graph[i]
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        ans += cost
print(ans)