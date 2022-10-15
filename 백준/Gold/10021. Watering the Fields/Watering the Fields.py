import sys
import heapq

n, base_cost = map(int, sys.stdin.readline().rstrip().split())
nodes = []
for _ in range(n): nodes.append(list(map(int, sys.stdin.readline().rstrip().split())))

parents = [i for i in range(n)]
pq = []

for i in range(n):
    for j in range(i+1, n):
        a, b = nodes[i]
        c, d = nodes[j]
        cost = abs(a-c)**2 + abs(b-d)**2
        if cost >= base_cost: heapq.heappush(pq, [cost, i, j])

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]
def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2: return False
    else:
        parents[root2] = root1
        return True

total = 0
edge_num = 0
while pq:
    cur_cost, node1, node2 = heapq.heappop(pq)

    if union(node1, node2):
        total += cur_cost
        edge_num += 1
        if edge_num == n-1: break

if edge_num == n-1: print(total)
else: print(-1)