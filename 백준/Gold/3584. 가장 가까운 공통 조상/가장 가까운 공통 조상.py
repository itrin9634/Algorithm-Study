t = int(input())

for _ in range(t):
    n = int(input())
    parent = [0] * (n+1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a
    x, y = map(int, input().split())
    x_parents = [0, x]
    y_parents = [0, y]
    while parent[x]:
        x_parents.append(parent[x])
        x = parent[x]
    while parent[y]:
        y_parents.append(parent[y])
        y = parent[y]
    i = 1
    while x_parents[-i] == y_parents[-i]:
        i += 1
    print(x_parents[-i+1])