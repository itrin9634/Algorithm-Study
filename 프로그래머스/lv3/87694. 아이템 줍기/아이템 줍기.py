from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX = 102
    board = [[5] * MAX for _ in range(MAX)]

    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 *2, x2 *2, y2 * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 0
                elif board[i][j] != 0:
                    board[i][j] = 1

    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    q = deque()
    q.append((characterX * 2, characterY * 2))
    visited = [[0] * MAX for _ in range(MAX)]
    visited[characterX * 2][characterY * 2] = 1
    while q:
        x, y = q.popleft()
        if x == 2 * itemX and y == 2 * itemY:
            answer = (visited[x][y] - 1) // 2
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not visited[nx][ny] and board[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return answer