from itertools import combinations
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
homes = []
chickens = []
MAX = 999999
result = MAX
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            homes.append((i, j))
        elif board[i][j] == 2:
            chickens.append((i, j))

combs = combinations(chickens, m)
for com in combs:
    tmp_city_length = 0
    for h in homes:
        hx, hy = h
        chick_length = MAX
        for chic in com:
            cx, cy = chic
            chick_length = min(chick_length, abs(hx-cx) + abs(hy-cy))
        tmp_city_length += chick_length
    result = min(result, tmp_city_length)
print(result)