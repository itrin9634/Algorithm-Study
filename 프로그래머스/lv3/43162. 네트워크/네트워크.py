from collections import deque

def bfs(start, visited, graph):
    q = deque([start])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            visited[i] = True
            bfs(i, visited, graph)
    return answer