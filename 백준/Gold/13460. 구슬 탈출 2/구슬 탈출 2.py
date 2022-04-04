n, m = map(int, input().split())
graph = [list(input().rstrip())for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
q = []

dx = [0, 0, -1, 1]  # 좌, 우, 상, 하
dy = [-1, 1, 0, 0]


def pos_init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':
                rx, ry = i, j
            elif graph[i][j] == 'B':
                bx, by = i, j
    visited[rx][ry][bx][by] = True
    q.append((rx, ry, bx, by, 1))


def move(x, y, dx, dy):
    cnt = 0
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def solve():
    pos_init()
    while q:
        rx, ry, bx, by, depth = q.pop(0)
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            if graph[nbx][nby] != 'O':
                if graph[nrx][nry] == 'O':
                    print(depth)
                    return
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, depth + 1))
    print(-1)


solve()
