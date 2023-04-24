from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    cq1 = deque(cards1)
    cq2 = deque(cards2)
    
    idx = 0
    cs1, cs2 = cq1.popleft(), cq2.popleft()
    
    while (cs1 or cs2) and idx < len(goal):
        if cs1 == goal[idx]:
            idx += 1
            if cq1:
                cs1 = cq1.popleft()
            else:
                cs1 = ''
            continue
        if cs2 == goal[idx]:
            idx += 1
            if cq2:
                cs2 = cq2.popleft()
            else:
                cs2 = ''
            continue
        
        return 'No'
    if idx == len(goal):
        return 'Yes'
    return 'No'