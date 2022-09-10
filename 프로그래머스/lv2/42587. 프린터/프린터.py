from collections import deque
def solution(priorities, location):
    answer = 0
    hash = {}
    q = deque()
    for i in range(len(priorities)):
        hash[i] = priorities[i]
        q.append((priorities[i], i))
    print(q)
    print(hash)
    cnt = 0
    while q:
        score, idx = q.popleft()
        MAX = max(hash.values())
        if MAX > score:
            q.append((score, idx))
        else:
            cnt += 1
            del hash[idx]
            if location == idx:
                return cnt