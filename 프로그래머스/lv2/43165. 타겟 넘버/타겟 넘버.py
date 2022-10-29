cnt = 0
def dfs(total, arr, idx, target):
    global cnt
    if idx == len(arr) - 1:
        if total == target:
            cnt += 1
        return
    dfs(total + arr[idx + 1], arr, idx + 1, target)
    dfs(total - arr[idx + 1], arr, idx + 1, target)

def solution(numbers, target):
    dfs(-numbers[0], numbers, 0, target)
    dfs(numbers[0], numbers, 0, target)
    return cnt