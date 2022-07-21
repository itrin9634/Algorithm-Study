n = int(input())
nums = list(map(int, input().split()))
#덧셈, 뺄셈, 곱셈, 나눗셈의 개수
opers = list(map(int, input().split()))
start = nums[0]
nums = nums[1:]
result = []


def cal(a, b, i):
    if i == 0:
        return a + b
    elif i == 1:
        return a - b
    elif i == 2:
        return a * b
    elif i == 3:
        return int(a / b)


def dfs(num, idx, opers):
    if idx == len(nums):
        result.append(num)
        return
    for i in range(4):
        if opers[i] == 0:
            continue
        opers[i] -= 1
        dfs(cal(num, nums[idx], i), idx+1, opers)
        opers[i] += 1


dfs(start, 0, opers)
print(max(result))
print(min(result))