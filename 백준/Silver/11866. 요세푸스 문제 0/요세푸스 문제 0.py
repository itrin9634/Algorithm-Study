from collections import deque
n, k = map(int, input().split())
q = deque(range(1, n+1))
result = []
while q:
    for i in range(k-1):
        x = q.popleft()
        q.append(x)
    num = q.popleft()
    result.append(str(num))
print("<"+', '.join(result)+">")