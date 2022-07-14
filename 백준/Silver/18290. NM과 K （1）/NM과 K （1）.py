import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = -100000
visited = [[False] * m for _ in range(n)]

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def sol(x, y, idx, tmp_sum):
    global result

    if idx == k:
        result = max(result, tmp_sum)
        return

    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            if visited[i][j]:
                continue

            ok = True
            for q in range(4):
                nx = i + dx[q]
                ny = j + dy[q]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                    ok = False
                    break
            if ok:
                visited[i][j] = True
                sol(i, j, idx+1, tmp_sum + board[i][j])
                visited[i][j] = False


sol(0, 0, 0, 0)
print(result)