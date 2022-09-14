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
            heapq.heappop(q)
        elif a == 'D' and int(b) == -1:
            heapq.heappop(q1)
    MAX = -int(1e9)
    MIN = int(1e9)
    print(q)
    print(q1)
    for i in range(len(q1)):
        num, idx = q1[i]
        if any(idx == x[1] for x in q):
            print(idx)
            MAX = max(MAX, num)
            MIN = min(MIN, num)
    print(MAX, MIN)
    if (MAX != -int(1e9)) or (MIN != int(1e9)):
        print('1111')
        return [MAX, MIN]
    else:
        return [0, 0]
  