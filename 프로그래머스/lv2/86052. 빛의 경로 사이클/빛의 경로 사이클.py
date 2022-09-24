def solution(grid):
    answer = []
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    lx, ly = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(ly)] for _ in range(lx)]
    
    for i in range(lx):
        for j in range(ly):
            for d in range(4):
                if visited[i][j][d]:
                    continue
                cnt = 0
                nx, ny = i, j
                while not visited[nx][ny][d]:
                    visited[nx][ny][d] = True
                    cnt += 1
                    if grid[nx][ny] == 'S':
                        pass
                    elif grid[nx][ny] == 'L':
                        d = (d-1) % 4
                    elif grid[nx][ny] == 'R':
                        d = (d+1) % 4
                    nx, ny = (nx + dx[d]) % lx, (ny + dy[d]) % ly
                answer.append(cnt)
    answer.sort()
    return answer