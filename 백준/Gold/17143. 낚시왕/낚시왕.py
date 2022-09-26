r, c, m = map(int, input().split())
arr = [[0] * c for _ in range(r)]
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    arr[x-1][y-1] = (s, d, z)


# 물고기 잡기
def fish(j):
    for i in range(r):
        if arr[i][j]:
            x = arr[i][j][2]
            arr[i][j] = 0
            return x
    return 0


def get_next_loc(i, j, speed, dir):
    if dir == up or dir == down:
        cycle = r * 2 - 2
        if dir == up:
            speed += 2 * ( r - 1) - i
        else:
            speed += i
        speed %= cycle
        if speed >= r:
            return (2 * r - 2 - speed, j, up)
        return (speed, j, down)
    else:
        cycle = c * 2 - 2
        if dir == left:
            speed += 2 * (c-1) - j
        else:
            speed += j
        speed %= cycle
        if speed >= c:
            return (i, 2 * c - 2 - speed, left)
        return (i, speed, right)


#상어 이동
def move():
    global arr
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j]:
                ni, nj, nd = get_next_loc(i, j, arr[i][j][0], arr[i][j][1])
                if temp[ni][nj]:
                    temp[ni][nj] = max(
                        temp[ni][nj],
                        (arr[i][j][0], nd, arr[i][j][2]),
                        key = lambda x: x[2],
                    )
                else:
                    temp[ni][nj] = (arr[i][j][0], nd, arr[i][j][2])
    arr = temp


up, down, right, left = 1, 2, 3, 4
ans = 0
for j in range(c):
    ans += fish(j)
    move()
print(ans)