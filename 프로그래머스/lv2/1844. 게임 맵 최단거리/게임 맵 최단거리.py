from collections import deque

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(maps):
    n, m = len(maps), len(maps[0])
    answer = int(1e9)
    q = deque()
    q.append((0, 0, 1)) # x, y, 지나온 칸
    maps[0][0] = -2
    while q:
        x, y, cost = q.popleft()
        if x == n-1 and y == m-1:
            answer = min(answer, cost)
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = -2
                    q.append((nx, ny, cost + 1))
    
    if answer == int(1e9):
        return -1
    else:
        return answer