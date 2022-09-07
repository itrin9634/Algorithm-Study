from collections import deque
def solution(s):
    answer = 0
    tmp = []
    q = deque(list(s))
    while q:
        now = q.popleft()
        if tmp and now == tmp[-1]:
            tmp.pop()
        else:
            tmp.append(now)
            
    if not tmp:
        answer = 1
    
    return answer