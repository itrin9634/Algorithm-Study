import heapq

n = int(input())
q = []
for i in range(n):
    heapq.heappush(q, int(input()))

result = 0
while len(q) >= 2:
    fir = heapq.heappop(q)
    sec = heapq.heappop(q)
    result += fir+sec
    heapq.heappush(q, fir+sec)

print(result)