from collections import deque

def bfs(node, tree, visited, w):
    cnt = 0
    visited[node] = True
    q = deque()
    q.append(node)
    
    while q:
        node = q.popleft()
        cnt += 1
        for i in tree[node]:
            if (node == w[0] and i == w[1]) or (i == w[0] and node == w[1]):
                continue
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return cnt   
    


def solution(n, wires):
    answer = int(1e9)
    tree = [[] for _ in range(n+1)]
    for w in wires:
        a, b = w
        tree[a].append(b)
        tree[b].append(a)
    
    for w in wires:
        temp = []
        visited = [False] * (n+1)
        for i in range(1, n+1):
            if not visited[i]:
                cnt = bfs(i, tree, visited, w)
                temp.append(cnt)
        answer = min(answer, abs(temp[0] - temp[1]))
        
    
    return answer