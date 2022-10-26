import sys
input = sys.stdin.readline

n, k = map(int, input().split())
color_map = [list(map(int, input().split())) for _ in range(n)]
chess_map = [[[] for _ in range(n)] for _ in range(n)]
chess = [i for i in range(k)]

#체스 정보 입력
for i in range(k):
    x, y, d = map(int, input().split())
    chess_map[x-1][y-1].append(i)
    chess[i] =  [x-1, y-1, d-1]

#방향 우 좌 상 하
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def move(i):
    #가장 아래에 있는지 확인
    x, y, d = chess[i]
    if chess_map[x][y][0] != i:
        return False

    #다음 이동 칸
    nx = x + dx[d]
    ny = y + dy[d]
    if not 0 <= nx < n or not 0 <= ny < n or color_map[nx][ny] == 2:
        #범위벗어나거나 파란색인 경우 방향 바꾸기
        if d == 0 or d == 2:
            nd = d + 1
        else:
            nd = d - 1
        nx = x + dx[nd]
        ny = y + dy[nd]

        # 방향 바꾸기
        chess[i][-1] = nd
        if not 0 <= nx < n or not 0 <= ny < n or color_map[nx][ny] == 2:
            return False

    chess_set = []
    chess_set.extend(chess_map[x][y])
    chess_map[x][y] = []
    if color_map[nx][ny] == 1:
        chess_set = chess_set[::-1]

    for i in chess_set:
        chess_map[nx][ny].append(i)
        chess[i][:2] = [nx, ny] # chess i는 nx, ny에 위치해 있다 표시
    if len(chess_map[nx][ny]) >= 4:
        return True
    return False


cnt = 0
while cnt <= 1000:
    cnt += 1
    for i in range(k):
        flag = move(i)
        if flag:
            print(cnt)
            sys.exit()
print(-1)