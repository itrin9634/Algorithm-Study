n = int(input())
arr = list(map(int, input().split()))
ops = list(map(int, input().split()))
min_ans = int(1e9)
max_ans = -int(1e9)


def cal(a, b, idx):
    if idx == 0:
        return a + b
    elif idx == 1:
        return a - b
    elif idx == 2:
        return a * b
    elif idx == 3:
        if a > 0:
            return a // b
        else:
            return -((-a) // b)


def dfs(now, idx):
    global min_ans, max_ans
    if idx == n:
        min_ans = min(now, min_ans)
        max_ans = max(now, max_ans)
        return
    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            dfs(cal(now, arr[idx], i), idx + 1)
            ops[i] += 1


dfs(arr[0], 1)
print(max_ans)
print(min_ans)

