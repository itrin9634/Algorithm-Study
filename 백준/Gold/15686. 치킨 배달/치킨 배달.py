from itertools import combinations
n, m = map(int, input().split())
graph = [input().split() for _ in range(n)]
homes = []
chickens = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            homes.append([i, j])
        if graph[i][j] == '2':
            chickens.append([i, j])
INF = int(1e9)
result = INF
for ch in combinations(chickens, m):
    r = 0
    for h in homes:
        length = INF
        for c in ch:
            temp = abs(h[0]-c[0]) + abs(h[1] - c[1])
            length = min(temp, length)
        r += length
    result = min(result, r)
print(result)

