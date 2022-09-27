from collections import deque

n = int(input())
arr = list(map(int, input().split()))
r_node = int(input())
tree = [[] for _ in range(n)]
root = 0
for i in range(len(arr)):
    if arr[i] != -1:
        tree[arr[i]].append(i)
    else:
        root = i
ans = 0
if root != r_node:
    q = deque([root])
    while q:
        now = q.popleft()
        cnt = 0
        for i in tree[now]:
            if i != r_node:
                cnt += 1
                q.append(i)
        if cnt == 0:
            ans += 1
print(ans)
