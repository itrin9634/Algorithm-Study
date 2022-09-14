import heapq
def solution(operations):
    q = [] #최대힙
    q1 = [] #최소힙
    for i in range(len(operations)):
        a, b = operations[i].split()
        if a == 'I':
            heapq.heappush(q, (-int(b), i))
            heapq.heappush(q1, (int(b), i))
        elif a == 'D' and int(b) == 1:
            if q:
                num, idx = heapq.heappop(q)
                q1.remove((-num, idx))
        elif a == 'D' and int(b) == -1:
            if q1:
                num, idx = heapq.heappop(q1)
                q.remove((-num, idx))
    if q1:
        MAX = max(x[0] for x in q1)
        MIN = min(x[0] for x in q1)
        return [MAX, MIN]
    else:
        return [0, 0]
    
  