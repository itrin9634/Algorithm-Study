from collections import Counter

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, wires):
    ans = n
    for i in range(len(wires)):
        tmp = wires[:i] + wires[i+1:]
        parent = [i for i in range(n+1)]
        for wire in tmp:
            if find_parent(parent, wire[0]) == find_parent(parent, wire[1]):
                continue
            union_parent(parent, wire[0], wire[1])            
        
        uf = []
        for i in range(1, n + 1):
            uf.append(find_parent(parent, i))
        uf = Counter(uf)
        v = list(uf.values())
        ans = min(ans, abs( v[0]- v[1]))
    return ans