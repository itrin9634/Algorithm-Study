from collections import deque
def isChange(now, new_word):
    for i in range(len(now)):
        if now[:i] == new_word[:i] and now[i+1:] == new_word[i+1:]:
            return True
    return False

def solution(begin, target, words):
    answer = int(1e9)
    visited = [False] * len(words)
    if target not in words:
        return 0
    now = begin
    q = deque()
    for i in range(len(words)):
        if not visited[i] and isChange(now, words[i]):
            visited[i] = True
            q.append((words[i], 1))
    while q:
        x, cnt = q.popleft()
        if x == target:
            answer = min(answer, cnt)
        for i in range(len(words)):
            if not visited[i] and isChange(x, words[i]):
                visited[i] = True
                q.append((words[i], cnt + 1))
    if answer == int(1e9):
        return 0
    else:
        return answer