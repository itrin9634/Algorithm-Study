from collections import deque

def solution(arr):
    answer = []
    answer.append(arr[0])
    if len(arr) > 1:
        q = deque(arr[1:])
        while q:
            now = q.popleft()
            if now != answer[-1]:
                answer.append(now)
    return answer