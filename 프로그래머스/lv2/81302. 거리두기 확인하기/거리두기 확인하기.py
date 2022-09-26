from collections import deque

def bfs(p):
    start = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append((i, j))
    
    for s in start:
        q = deque([s])
        visited = [[False] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        visited[s[0]][s[1]] = True
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    if p[nx][ny] == 'O':
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        distance[nx][ny] = distance[x][y] + 1
                    if p[nx][ny] == 'P' and distance[x][y] <= 1:
                        return 0
    return 1
def solution(places):
    answer = []
    for i in range(len(places)):
        answer.append(bfs(places[i]))
    return answer