from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    q = deque()
    for i in range(len(speeds)):
        q.append(math.ceil((100 - progresses[i]) / speeds[i]))
    cnt = 1
    day = q.popleft()
    while q:
        tmp = q.popleft()
        if day < tmp:
            day = tmp
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
    return answer