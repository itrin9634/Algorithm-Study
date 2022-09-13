n = int(input())
ops = []
dots = []
board = [[0] * 101 for _ in range(101)]
MAX = 101
# 우상좌하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


# 방향 구하는 함수
def get_ops(arr, g, now):
    global ops
    if now == g:
        ops = arr
        return
    tmp_ops = []
    for i in range(len(arr)):
        tmp_ops.append((arr[i] + 1) % 4)
    tmp_ops = tmp_ops[::-1]
    get_ops(arr + tmp_ops, g, now + 1)


# 점 구하는 함수
def check_dots(arr, x, y):
    board[x][y] = 1
    for i in range(len(arr)):
        nx = x + dx[arr[i]]
        ny = y + dy[arr[i]]
        if 0 <= nx <= 100 and 0 <= ny <= 100:
            board[nx][ny] = 1
            x, y = nx, ny


for i in range(n):
    dots = []
    x, y, d, g = map(int, input().split())
    ops = [d]
    get_ops([d], g, 0)
    y, x = x, y
    check_dots(ops, x, y)


# 정사각형의 네 꼭짓점 확인
def check(x, y):
    tmp = [(x, y), (x, y+1), (x+1, y), (x+1, y+1)]
    for i in range(4):
        a, b = tmp[i]
        if 0 <= a <= 100 and 0 <= b <= 100 and board[a][b] == 1:
            continue
        else:
            return False
    return True

cnt = 0
for i in range(100):
    for j in range(100):
        if check(i, j):
            cnt += 1
print(cnt)
