n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cmd = list(map(int, input().split()))
floor = 0

#동서북남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#위 동 서 앞 뒤 바닥
dice = [0, 0, 0, 0, 0, 0]


def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


for c in cmd:
    nx = x + dx[c-1]
    ny = y + dy[c-1]

    if 0 <= nx < n and 0 <= ny < m:
        turn(c)
        if arr[nx][ny] == 0:
            arr[nx][ny] = dice[5]
        else:
            dice[5] = arr[nx][ny]
            arr[nx][ny] = 0
        x, y = nx, ny
        print(dice[0])