import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
opers = list(map(int, input().split()))

def op1():
    new_arr = [[0] * m for _ in range(n)]
    for i in range(n):
        new_arr[i] = arr[n - 1 - i]
    return new_arr


def op2():
    new_arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_arr[i][j] = arr[i][m - 1 - j]
    return new_arr


def op3(arr, n, m):
    new_arr = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_arr[i][j] = arr[n - j - 1][i]
    return new_arr


def op4(arr, n, m):
    new_arr = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_arr[i][j] = arr[j][m - i - 1]
    return new_arr


def op5():
    new_arr = [[0] * m for _ in range(n)]
    half_n = n // 2
    half_m = m // 2
    # 1번그룹
    for i in range(half_n):
        for j in range(half_m):
            new_arr[i][j] = arr[half_n+i][j]  # 1번
            new_arr[i][half_m + j] = arr[i][j]  # 2번
            new_arr[half_n + i][half_m + j] = arr[i][half_m + j]  # 3번
            new_arr[half_n + i][j] = arr[half_n + i][half_m + j]  # 4 번
    return new_arr


def op6():
    new_arr = [[0] * m for _ in range(n)]
    half_n = n // 2
    half_m = m // 2
    # 1번그룹
    for i in range(half_n):
        for j in range(half_m):
            new_arr[i][j] = arr[i][half_m + j]  # 1번
            new_arr[i][half_m + j] = arr[half_n + i][half_m + j]  # 2번
            new_arr[half_n + i][half_m + j] = arr[i + half_n][j]  # 3번
            new_arr[half_n + i][j] = arr[i][j]  # 4 번
    return new_arr


for op in opers:
    if op == 1:
        arr = op1()
    elif op == 2:
        arr = op2()
    elif op == 3:
        arr = op3(arr, n, m)
        n, m = m, n
    elif op == 4:
        arr = op4(arr, n, m)
        n, m = m, n
    elif op == 5:
        arr = op5()
    elif op == 6:
        arr = op6()

for i in arr:
    print(*i)