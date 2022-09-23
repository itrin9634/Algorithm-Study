n, m, k = map(int, input().split())
plus_a = [list(map(int, input().split())) for _ in range(n)] #양분

trees = [[[] for _ in range(n)] for _ in range(n)]
food = [[5] * n for _ in range(n)] #양분

for i in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

for year in range(k):

    # 봄 , 여름
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                trees[i][j].sort()
                temp_tree, dead_tree = [], 0
                for age in trees[i][j]:
                    if food[i][j] >= age:
                        food[i][j] -= age
                        age += 1
                        temp_tree.append(age)
                    else:
                        dead_tree += (age // 2)
                food[i][j] += dead_tree
                trees[i][j] = []
                trees[i][j].extend(temp_tree)

    #가을
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for age in trees[i][j]:
                    if age % 5 == 0:
                        for dir in range(8):
                            ni = i + dx[dir]
                            nj = j + dy[dir]
                            if 0 <= ni < n and 0 <= nj < n:
                                trees[ni][nj].append(1)
    #겨울
    for i in range(n):
        for j in range(n):
            food[i][j] += plus_a[i][j]


# 최종 나무 세기
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(trees[i][j])
print(cnt)

