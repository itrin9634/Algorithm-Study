from copy import deepcopy
r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

up = -1
down = -1

# 공기 청정기 위치 찾기
for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break


# 미세먼지 확산
def spread():
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        tmp_arr[nx][ny] += arr[i][j] // 5
                        tmp += arr[i][j] // 5
                arr[i][j] -= tmp
    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp_arr[i][j]


def air_up():
    # 반시계 방향 (동 북 서 남)
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x, y = nx, ny


def air_down():
    # 시계 방향 (동 남 서 북)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x, y = nx, ny


for _ in range(t):
    spread()
    air_up()
    air_down()

ans = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            ans += arr[i][j]
print(ans)