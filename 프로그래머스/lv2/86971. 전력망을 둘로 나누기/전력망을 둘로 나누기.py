from collections import deque

def bfs(start, graph, visited, wire, cnt):
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        now = q.popleft()
        cnt += 1
        for i in graph[now]:
            if (now == wire[0] and i == wire[1]) or (now == wire[1] and i == wire[0]):
                continue
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return cnt

def solution(n, wires):
    ans = n
    graph = [[] for _ in range(n+1)]
    for w in wires:
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])
    
    for wire in wires:
        visited = [False] * (n+1)
        temp = []
        for i in range(1, n+1):
            if not visited[i]:
                cnt = bfs(i, graph, visited, wire, 0)
                temp.append(cnt)
        ans = min(ans, abs(temp[0] - temp[1]))    
    return ans