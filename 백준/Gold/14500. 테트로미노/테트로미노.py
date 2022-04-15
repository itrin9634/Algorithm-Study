n, m = map(int, input().split(' '))

maps = [list(map(int, input().split(' '))) for _ in range(n)]
check = [[True]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
max_result = -1

# 재귀함수로 가능한 사각형
def go(x, y, now, cnt):
    global max_result
    
    # 정사각형이 4개가 되면 최대값과 비교하고 dfs 종료
    if cnt == 4:
        if now > max_result:
            max_result = now
        return

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < n and 0 <= new_y < m:
            if check[new_x][new_y]:
                check[new_x][new_y] = False
                go(new_x, new_y, now+maps[new_x][new_y], cnt+1)
                check[new_x][new_y] = True

# 재귀함수로 불가능한 사각형
def nogo(x, y):
    # 가운데 값 고정
    center = maps[x][y]
    
    # 상하좌우 날개
    wings = 4

    min_result = 100000

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        
        # 날개가 2개면 테트로미노를 만들지 못하므로 종료
        if wings == 2:
            return 0
        
        # 범위를 벗어난 경우 날개 1개 감소
        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
            wings -= 1
            continue
        
        # 범위를 벗어나지 않았다면 값을 더해주고 해당 값이 최소값인지 찾는다
        center += maps[new_x][new_y]
        if maps[new_x][new_y] < min_result:
            min_result = maps[new_x][new_y]
    
    # 날개가 4개의 경우 총 5개의 정사각형이므로 가장 최소값인 사각형 1개를 빼준다
    if wings == 4:
        center -= min_result

    return center


for i in range(n):
    for j in range(m):
        check[i][j] = False
        go(i, j, maps[i][j], 1)
        check[i][j] = True

        temp = nogo(i, j)
        if temp > max_result:
            max_result = temp

print(max_result)