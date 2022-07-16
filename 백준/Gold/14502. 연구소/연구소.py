n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
tmp = [[0] * m for _ in range(n)] #벽을 설치한 뒤의 맵 리스트

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0


# 안전 구역 세는 함수
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                score += 1
    return score


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
            tmp[nx][ny] = 2
            virus(nx, ny)
    return


def dfs(cnt):
    global result

    if cnt == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                cnt += 1
                dfs(cnt)
                data[i][j] = 0
                cnt -= 1

                
dfs(0)
print(result)
