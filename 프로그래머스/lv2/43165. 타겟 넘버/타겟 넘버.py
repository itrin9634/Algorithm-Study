from collections import deque

cnt = 0

def dfs(i, now, target, arr):
    global cnt
    if i == len(arr)-1:
        if now == target:
            cnt += 1
        return
    dfs(i+1, now + arr[i+1], target, arr)
    dfs(i+1, now - arr[i+1], target, arr)
    
    
def solution(numbers, target):
    answer = 0
    dfs(0, numbers[0], target, numbers)
    dfs(0, -numbers[0], target, numbers)            
            
    return cnt