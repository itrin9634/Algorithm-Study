cnt = 1
def dfs(idx, n, total):
    global cnt
    if total == n:
        cnt += 1
        return
    if total < n and idx <= (n//2) + 1:
        dfs(idx + 1, n, total + idx)


def solution(n):
    global cnt
    for i in range(1, (n // 2) + 1):
        dfs(i+1, n, i)
        
    return cnt