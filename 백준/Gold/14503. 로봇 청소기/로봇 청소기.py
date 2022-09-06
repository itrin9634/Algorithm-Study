from collections import deque
import sys
input = sys.stdin.readline

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def bfs(a, b, d):
    cnt = 0
    q = deque()
    q.append((a, b, d))
    arr[a][b] = 2
    cnt += 1

    while q:
        x, y, d = q.popleft()
        tmp_d = d
        turn = 0

        for i in range(4):
            nd = (tmp_d + 3) % 4
            nx, ny = x + dx[nd], y + dy[nd]
            tmp_d = nd
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                q.append((nx, ny, nd))
                arr[nx][ny] = 2
                cnt += 1
                break
            else:
                turn += 1
        if turn == 4:
            bx, by = x + dx[(d + 2) % 4], y + dy[(d+2) % 4]
            if arr[bx][by] == 1:
                return cnt
            q.append((bx, by, d))


print(bfs(r, c, d))
