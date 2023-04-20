import heapq

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(maps):
    x, y = -1, -1
    visited = [[[0 for _ in range(2)] for _ in range(len(maps[0]))]for _ in range(len(maps))] 
    # 시작점 설정
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                x, y = i, j
                break
    h = []
    heapq.heappush(h, (0, x, y, 0, visited))
    
    while h:
        d, x, y, l, v = heapq.heappop(h)
        v[x][y][l] = 1
        
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            td, tl = d+1, l
            if not(0 <= tx < len(maps)) or not(0 <= ty < len(maps[0])) or maps[tx][ty] == 'X':
                continue
            if maps[tx][ty] == 'L':
                tl = 1
            if v[tx][ty][tl] :
                continue
            if maps[tx][ty] == 'E' and tl:
                return td
            v[tx][ty][tl] = 1
            heapq.heappush(h, (td, tx, ty, tl, v))
    
    return -1