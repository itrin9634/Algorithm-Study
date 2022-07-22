from itertools import combinations
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
numbers = [i for i in range(n)]
result = int(1e9)

for i in range(1, n//2 + 1):
    combs = list(combinations(numbers, i))
    for start_members in combs:
        link_mebers = list(set(numbers) - set(start_members))
        start_score, link_score = 0, 0
        for i in start_members:
            for j in start_members:
                start_score += graph[i][j]
        for i in link_mebers:
            for j in link_mebers:
                link_score += graph[i][j]
        result = min(result, abs(start_score - link_score))

print(result)