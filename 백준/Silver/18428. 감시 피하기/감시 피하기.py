n = int(input())
graph = [list(input().split()) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

teachers = []


# 학생 찾기
def check_s(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        while 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 'O':
            if graph[nx][ny] == 'S':
                return True #감시 가능함
            nx += dx[i]
            ny += dy[i]
    return False


def dfs(count):
    global answer
    if count == 3:
        cnt = 0
        for t in teachers:
            tx, ty = t
            if not check_s(tx, ty):
                cnt += 1
        if cnt == len(teachers):
            answer = True
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                count += 1
                dfs(count)
                graph[i][j] = 'X'
                count -= 1


# 선생님 위치 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i, j))

answer = False
dfs(0)
if answer:
    print('YES')
else:
    print('NO')
