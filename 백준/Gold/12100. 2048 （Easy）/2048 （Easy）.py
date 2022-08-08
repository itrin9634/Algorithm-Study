from copy import deepcopy
import sys
input = sys.stdin.readline


def up(arr):
    for j in range(n):
        p = 0
        for i in range(1, n):
            if arr[i][j]:
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[p][j] == 0:
                    arr[p][j] = tmp
                elif arr[p][j] == tmp:
                    arr[p][j] *= 2
                    p += 1
                else:
                    p += 1
                    arr[p][j] = tmp
    return arr


def down(arr):
    for j in range(n):
        p = n-1
        for i in range(n-2, -1, -1):
            if arr[i][j]:
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[p][j] == 0:
                    arr[p][j] = tmp
                elif arr[p][j] == tmp:
                    arr[p][j] *= 2
                    p -= 1
                else:
                    p -= 1
                    arr[p][j] = tmp
    return arr


def left(arr):
    for i in range(n):
        p = 0
        for j in range(1, n):
            if arr[i][j]:
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[i][p] == 0:
                    arr[i][p] = tmp
                elif arr[i][p] == tmp:
                    arr[i][p] *= 2
                    p += 1
                else:
                    p += 1
                    arr[i][p] = tmp
    return arr


def right(arr):
    for i in range(n):
        p = n-1
        for j in range(n-2, -1, -1):
            if arr[i][j]:
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[i][p] == 0:
                    arr[i][p] = tmp
                elif arr[i][p] == tmp:
                    arr[i][p] *= 2
                    p -= 1
                else:
                    p -= 1
                    arr[i][p] = tmp
    return arr


def dfs(board, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return

    dfs(up(deepcopy(board)), cnt + 1)
    dfs(down(deepcopy(board)), cnt + 1)
    dfs(left(deepcopy(board)), cnt + 1)
    dfs(right(deepcopy(board)), cnt + 1)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(graph, 0)
print(ans)