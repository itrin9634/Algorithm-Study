from itertools import combinations
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
numbers = [i for i in range(n)]
start_mems = list(combinations(numbers, n//2))
result = int(1e9)

for s in start_mems:
    link_mems = list(set(numbers) - set(s))
    total_start, total_link = 0, 0

    for i in s:
        for j in s:
            total_start += graph[i][j]

    for i in link_mems:
        for j in link_mems:
            total_link += graph[i][j]
    result = min(abs(total_link - total_start), result)

print(result)